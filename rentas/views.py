# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Renta,Galeria,Reservacion,Comentarios,Provincia,Municipio
from rentas.forms import FormularioReservas,FormularioComentario,FormularioFiltro
from django.db.models import Q
from datetime import date
import json as simplejson
import datetime
from django.core.mail import EmailMessage
import cmghostal.settings as siteSet
import cmghostal.crypter as crypter
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.translation import ugettext as _



# Create your views here.
def ultimas(request):
    list_rentas = Renta.objects.all().order_by('-id')[0:3]
    return render(request, 'ultimas.html', {'rentas': list_rentas})

def detalles(request,offset):
    list_rentas = Renta.objects.filter(id=offset)
    for renta in list_rentas:
        list_comentarios = Comentarios.objects.filter(renta = renta)
    if request.method == 'POST':

        if 'nombre' in request.POST:
            formcomentario = FormularioComentario(request.POST)
            if formcomentario.is_valid():
                cd = formcomentario.cleaned_data
                renta = Renta.objects.get(id=offset)
                nuevo_comentario = Comentarios.objects.create(nombre = cd['nombre'],
                                                            comentario = cd['comentario'],
                                                            fecha = date.today(),
                                                            renta = renta)
                nuevo_comentario.save()
                formcomentario = FormularioComentario()
        else:
            formcomentario = FormularioComentario()

        if 'nombre_cliente' in request.POST:
            form = FormularioReservas(request.POST)
            if form.is_valid():
                cd = form.data
                renta = Renta.objects.get(id=offset)
                reserva = Reservacion.objects.filter(Q(renta=renta), Q(
                    fecha_entrada__range=(cd['fecha_entrada'], cd['fecha_salida'])) | Q(
                    fecha_salida__range=(cd['fecha_entrada'], cd['fecha_salida'])))
                salida = " "
                if reserva.count() == 0:
                    nueva_reserva = Reservacion.objects.create(fecha_entrada=cd['fecha_entrada'],
                                                               fecha_salida=cd['fecha_salida'],
                                                               nombre_cliente=cd['nombre_cliente'],
                                                               email_cliente=cd['email_cliente'],
                                                               cantidad_personas=cd['cantidad_personas'],
                                                               renta=renta)
                    nueva_reserva.save()
                    id_reserva = crypter.EncriptarCadena(str(nueva_reserva.id))
                    nombre_cliente = crypter.EncriptarCadena(nueva_reserva.nombre_cliente)
                    email_cliente = crypter.EncriptarCadena(nueva_reserva.email_cliente)
                    asunto = _("Confirmación de reserva")
                    cuerpo = "<p>Se ha hecho una reserva para una de nuestras casas de renta y se ha especificado este correo para contacto, si no fue usted quien hizo la reserva "
                    cuerpo += "por favor ignore este mensaje de lo contrario le pedimos que confirme su reserva en el vículo especificado mas abajo, gracias por elegirnos. \n </p>"
                    cuerpo += " <a href=\"http://cmghostal.pythonanywhere.com/rentas/confirmacion/"+id_reserva+","+nombre_cliente+","+email_cliente+"\">Confirme su reserva</a>"
                    para = cd['email_cliente']
                    msg = EmailMessage(asunto, cuerpo, siteSet.DEFAULT_FROM_EMAIL, [para])
                    msg.content_subtype ="html"
                    msg.send()
                    salida = True
                else:
                    salida = False
                form = FormularioReservas()
                formcomentario = FormularioComentario()
                return render(request,'detalles.html', {'rentas':list_rentas,'form': form,'formcomentario':formcomentario,'salida':salida,'comentarios':list_comentarios})
        else:
            form = FormularioReservas()

        return render(request,'detalles.html', {'rentas':list_rentas,'form': form,'formcomentario':formcomentario,'comentarios':list_comentarios})
    else:
        form = FormularioReservas()
        formcomentario = FormularioComentario()


    return render(request, 'detalles.html', {'rentas': list_rentas,'form': form,'formcomentario':formcomentario,'comentarios':list_comentarios})

def formulario_reserva(request):
    if request.method == 'POST':
        form=FormularioReservas(request.POST)
        if form.is_valid():
            salida = "Exito con la reserva"
            return HttpResponseRedirect('formulario_reserva.html',{'form':form, 'salida':salida})
    else:
        form = FormularioReservas()
    return render(request,'detalles.html',{'form':form})

def confirmacion(request,reservacion):
    r=reservacion.split(",")\
    #id_res = crypter.DesEncriptarCadena(r[0])
    reserva = Reservacion.objects.get(id=crypter.DesEncriptarCadena(r[0]))
    if reserva.confirmado == False:
        reserva.confirmado = True
        reserva.save()

        asunto = "Confirmación de reserva"
        cuerpo = "<p>Se ha confirmado una reserva para "+reserva.renta.nombre+" desde "+str(reserva.fecha_entrada)+" hasta "+str(reserva.fecha_salida)+" por el cliente "+reserva.nombre_cliente+" con correo "+reserva.email_cliente
        cuerpo += " por favor verificar con la renta si hay disponibilidad y responder al cliente. \n </p>"
        msg = EmailMessage(asunto, cuerpo, siteSet.DEFAULT_FROM_EMAIL, [siteSet.DEFAULT_FROM_EMAIL])
        msg.content_subtype ="html"
        msg.send()

    return render(request,'confirmacion.html',{'reserva':reserva})

@login_required
@permission_required('rentas.change_reservacion')
def verificacion(request):
    reservaciones=Reservacion.objects.filter(confirmado=True).filter(verificado=False)
    return render(request,"verificacion.html",{'reservaciones':reservaciones})

@login_required
@permission_required('rentas.change_reservacion')
def verificado(request,id_reservacion):
    reservacion=Reservacion.objects.get(id=id_reservacion)
    reservacion.verificado=True
    reservacion.save()
    asunto = "Reserva para "+reservacion.renta.nombre
    cuerpo = "<p>Estimado "+reservacion.nombre_cliente+", tenemos el placer de informarle que la reservación hecha por usted para la renta "+reservacion.renta.nombre+" ha sido debidamente verificada "
    cuerpo += "por lo que usted puede viajar y hospedarse en la misma en la fecha "+str(reservacion.fecha_entrada.strftime("%d-%m-%Y"))+". \n </p>"
    cuerpo += "<p>Esperamos tenga una estancia agradable, gracias por elegirnos<p>"
    cuerpo += "<p>Atentamente el equipo de Tecnocasas<p>"
    para = reservacion.email_cliente
    msg = EmailMessage(asunto, cuerpo, siteSet.DEFAULT_FROM_EMAIL, [para])
    msg.content_subtype ="html"
    msg.send()
    return render(request,"verificado.html",{'reservacion':reservacion})

#TODO: Resolver el problema de la validacion del formulario. Consultar en Internet
#TODO: Resolver el problema del envio de correos.
#TODO: Metodo para enviar link encriptado

"""
    La idea general es que cuando se verifique una reserva se envie un correo
    al dueño del sitio que la confirmara previa consulta con la casa de renta
"""
def rentas_list(request):
    if request.method == 'POST':
        form = FormularioFiltro(request.POST)
        cd = form.data
        if cd['municipio']!='':
            list_rentas = Renta.objects.filter(municipio_id=cd['municipio'])
            fmunicipio=Municipio.objects.get(id=cd['municipio'])
            form = FormularioFiltro()
            rentas = rentas_paginadas(request.GET.get('page'),list_rentas)
            return render(request, 'lista.html', {'rentas': rentas,'form':form,'fmunicipio':fmunicipio})
        else:
            list_rentas = Renta.objects.all()
            form = FormularioFiltro()
            rentas = rentas_paginadas(request.GET.get('page'), list_rentas)
            return render(request, 'lista.html', {'rentas': rentas, 'form': form,})
        list_rentas = Renta.objects.all()
        form = FormularioFiltro()
        rentas = rentas_paginadas(request.GET.get('page'), list_rentas)
        return render(request, 'lista.html', {'rentas': rentas, 'form': form,})
    else:
        list_rentas = Renta.objects.all()
        form = FormularioFiltro()
        rentas = rentas_paginadas(request.GET.get('page'), list_rentas)
        return render(request, 'lista.html', {'rentas': rentas,'form':form,})

##Encontrar los municipios cuando se selecciona una provincia##
def encuentra_municipios(request):
    provincia = request.GET.get('provincia')
    ret = []
    if provincia:
        for municipio in Municipio.objects.filter(provincia_id=provincia):
            ret.append(dict(id=municipio.id, value=str(municipio)))
    if len(ret) != 1:
        ret.insert(0, dict(id='', value='(Seleccione un municipio)'))
    return HttpResponse(simplejson.dumps(ret),content_type='application/json')

##Paginacion de los datos de la renta##
def rentas_paginadas(page,list_rentas):

    paginator = Paginator(list_rentas, 10)
    try:
        rentas = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        rentas = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        rentas = paginator.page(paginator.num_pages)

    return rentas

def verificar(request,renta):
    renta_decrypted = crypter.DesEncriptarCadena(renta)
    return render(request, 'verificar.html',{'renta':renta_decrypted})
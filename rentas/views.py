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
                cd = form.cleaned_data
                entrada = datetime.date(int(cd['fecha_entrada_year']), int(cd['fecha_entrada_month']),
                                        int(cd['fecha_entrada_day']))
                salida = datetime.date(int(cd['fecha_salida_year']), int(cd['fecha_salida_month']),
                                       int(cd['fecha_salida_day']))

                if entrada < salida:
                    error_fecha = "La fecha de entrada es posterior a la de salida"
                if entrada < date.today():
                    error_fecha = "La fecha de entrada está en el pasado"

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
                    salida = "exito"
                else:
                    salida = "fracaso"
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

def rentas_list(request):
    if request.method == 'POST':
        form = FormularioFiltro(request.POST)
        cd = form.data
        if cd['municipio']!='':
            entrada = datetime.date(int(cd['fecha_entrada_year']),int(cd['fecha_entrada_month']),int(cd['fecha_entrada_day']))
            salida = datetime.date(int(cd['fecha_salida_year']),int(cd['fecha_salida_month']),int(cd['fecha_salida_day']))

            if entrada<salida:
                error_fecha="La fecha de entrada es posterior a la de salida"
            if entrada<date.today():
                error_fecha = "La fecha de entrada está en el pasado"

            list_rentas = Renta.objects.filter(municipio_id=cd['municipio'])
            fmunicipio=Municipio.objects.get(id=cd['municipio'])
            form = FormularioFiltro()
            rentas = rentas_paginadas(request.GET.get('page'),list_rentas)
            return render(request, 'lista.html', {'rentas': rentas,'form':form,'fmunicipio':fmunicipio})
        else:
            list_rentas = Renta.objects.all();
            form = FormularioFiltro()
            rentas = rentas_paginadas(request.GET.get('page'), list_rentas)
            return render(request, 'lista.html', {'rentas': rentas, 'form': form,})
    else:
        list_rentas = Renta.objects.all();
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
from django.shortcuts import render
from django.http import HttpResponseRedirect
from rentas.models import Renta
from django.contrib.auth.forms import UserCreationForm
from cmghostal.forms import FormularioContacto
from django.core.mail import send_mail
from . import settings as siteSet


def raiz(request):
    request.session['django_language'] = 'en'
    list_rentas = Renta.objects.all().order_by('-id')[0:3]
    return render(request, 'indice.html', {'rentas': list_rentas})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request,"registro.html",{'form':form,})

def contacto(request):
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            asunto = "Correo enviado por contactenos desde el sitio"
            cuerpo = "Mensaje enviado por: "
            cuerpo += cd['email']+" \n"
            cuerpo += cd['mensaje']
            de = cd['email']
            send_mail(asunto,cuerpo,de,["tecnocasas.53@gmail.com"])
            return render(request, "contacto.html", {'form': form,})
    else:
        form = FormularioContacto()
    return render(request, "contacto.html", {'form': form,})
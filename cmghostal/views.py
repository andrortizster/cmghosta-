from django.shortcuts import render
from django.http import HttpResponseRedirect
from rentas.models import Renta
from django.contrib.auth.forms import UserCreationForm


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
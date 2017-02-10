# -*- coding: utf-8 -*-
from django import forms

class FormularioReservas(forms.Form):
    fecha_entrada = forms.DateField(label="Fecha de entrada",widget=forms.SelectDateWidget)
    fecha_salida = forms.DateField(label="Fecha de salida",widget=forms.SelectDateWidget)
    nombre_cliente = forms.CharField(label="Nombre del cliente")
    email_cliente = forms.EmailField(label="Correo electrónico")
    cantidad_personas = forms.IntegerField(label="Cantidad de personas")

class FormularioComentario(forms.Form):
    nombre = forms.CharField(label="Escriba su nombre")
    comentario = forms.CharField(widget=forms.Textarea)

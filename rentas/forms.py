# -*- coding: utf-8 -*-
from django import forms
from rentas import models

class FormularioReservas(forms.Form):
    fecha_entrada = forms.DateField(label="Fecha de entrada",widget=forms.SelectDateWidget)
    fecha_salida = forms.DateField(label="Fecha de salida",widget=forms.SelectDateWidget)
    nombre_cliente = forms.CharField(label="Nombre del cliente")
    email_cliente = forms.EmailField(label="Correo electrónico")
    cantidad_personas = forms.IntegerField(label="Cantidad de personas")

class FormularioComentario(forms.Form):
    nombre = forms.CharField(label="Escriba su nombre")
    comentario = forms.CharField(widget=forms.Textarea)


class FormularioFiltro(forms.Form):
    provincia = forms.ModelChoiceField(models.Provincia.objects.all(), empty_label="(Seleccione una provincia)")
    municipio = forms.ModelChoiceField(models.Municipio.objects.none(), empty_label="(Seleccione un municipio)")
    fecha_entrada = forms.DateField(label="Fecha de entrada", widget=forms.SelectDateWidget)
    fecha_salida = forms.DateField(label="Fecha de salida", widget=forms.SelectDateWidget)
    dinero = forms.CharField(label="Máximo dinero a gastar")

    def __init__(self, *args, **kwargs):
        forms.Form.__init__(self, *args, **kwargs)
        provincias=models.Provincia.objects.all()
        if len(provincias)==1:
            self.fields['provincia'].initial=provincias[0].pk

        provincia_id=self.fields['provincia'].initial or self.initial.get('provincia')
        if provincia_id:
            municipios=models.Municipio.objects.filter(id=provincia_id)
            self.fields['municipios'].queryset=municipios
            if len(municipios)==1:
                self.fields['municipios'].initial=municipios[0].pk



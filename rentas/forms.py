# -*- coding: utf-8 -*-
from django import forms
from rentas import models
import datetime

class FormularioReservas(forms.Form):
    fecha_entrada = forms.DateField(label="Fecha de entrada", widget=forms.DateInput(attrs={'class': 'datepicker'}),required=True)
    fecha_salida = forms.DateField(label="Fecha de salida", widget=forms.DateInput(attrs={'class': 'datepicker'}),required=True)
    nombre_cliente = forms.CharField(label="Nombre del cliente",required=True)
    email_cliente = forms.EmailField(label="Correo electrónico",required=True)
    cantidad_personas = forms.IntegerField(label="Cantidad de personas",required=True)

    def clean_fecha_entrada(self):
        fecha_entrada=self.cleaned_data['fecha_entrada']
        fecha_salida=datetime.datetime.strptime(self.data['fecha_salida'],"%Y-%m-%d").date()
        if fecha_entrada > fecha_salida:
            raise forms.ValidationError("¡La fecha de entrada es mayor que la de salida!")
        if fecha_entrada < datetime.date.today():
            raise forms.ValidationError("¡La fecha de entrada está en el pasado!")
        return fecha_entrada

    def clean_fecha_salida(self):
        fecha_salida = self.cleaned_data['fecha_salida']
        if fecha_salida < datetime.date.today():
            raise forms.ValidationError("¡La fecha de salida está en el pasado!")
        return fecha_salida

class FormularioComentario(forms.Form):
    nombre = forms.CharField(label="Escriba su nombre")
    comentario = forms.CharField(widget=forms.Textarea)


class FormularioFiltro(forms.Form):
    provincia = forms.ModelChoiceField(models.Provincia.objects.all(), empty_label="(Seleccione una provincia)",required=True)
    municipio = forms.ModelChoiceField(models.Municipio.objects.none(), empty_label="(Seleccione un municipio)",required=True)
    fecha_entrada = forms.DateField(label="Fecha de entrada", widget=forms.DateInput(attrs={'class': 'datepicker'}))
    fecha_salida = forms.DateField(label="Fecha de salida", widget=forms.DateInput(attrs={'class': 'datepicker'}))
    dinero = forms.FloatField(label="Máximo dinero a gastar")

    def clean_fecha_entrada(self):
        if self.cleaned_data['fecha_entrada'] != '' and self.data['fecha_salida']!='':
            fecha_entrada = self.cleaned_data['fecha_entrada']
            fecha_salida = datetime.datetime.strptime(self.data['fecha_salida'], "%Y-%m-%d").date()
            if fecha_entrada > fecha_salida:
                raise forms.ValidationError("¡La fecha de entrada es mayor que la de salida!")
            if fecha_entrada < datetime.date.today():
                raise forms.ValidationError("¡La fecha de entrada está en el pasado!")
        return fecha_entrada

    def clean_fecha_salida(self):
        fecha_salida = self.cleaned_data['fecha_salida']
        if fecha_salida != '':
            if fecha_salida < datetime.date.today():
                raise forms.ValidationError("¡La fecha de salida está en el pasado!")
        return fecha_salida

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





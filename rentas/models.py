# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Provincia(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    nombre = models.CharField(max_length=30)
    provincia = models.ForeignKey(Provincia)

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=150)
    name = models.CharField(max_length=150,default='name of service')
    imagen = models.ImageField(upload_to='Servicios',null = True,blank = True)

    def __str__(self):
        return self.nombre

class Mes(models.Model):
    nombre = models.CharField(max_length=11)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural="Meses"

class Renta(models.Model):
    nombre = models.CharField(max_length=150)
    propietario = models.CharField(max_length=150)
    email = models.EmailField(blank=True,null=True)
    telefono = models.CharField(max_length=8,blank=True,null=True)
    movil = models.CharField(max_length=8,blank=True,null=True)
    direccion = models.TextField(verbose_name='Dirección',default = 'Dirección del inmueble')
    habitaciones = models.PositiveIntegerField()
    descripcion = models.TextField(verbose_name='Descripción',default = 'Escriba la descripción del inmueble')
    description = models.TextField(verbose_name='Descripción en Ingles',default = 'Enter property description')
    descrizione = models.TextField(verbose_name='Descripción en Italiano',default = 'Digitare la descrizione della proprietà')
    municipio = models.ForeignKey(Municipio)
    imagen = models.ImageField(upload_to='rentas',null = True,blank = True)
    precio_ta = models.FloatField(default=0)
    precio_tb = models.FloatField(default=0)
    meses_ta = models.ManyToManyField(Mes,verbose_name='Meses Temp. Alta')
    servicio = models.ManyToManyField(Servicio,verbose_name='Servicios')

    def __str__(self):
        return self.nombre

class Galeria(models.Model):
    renta = models.ForeignKey(Renta)
    imagen = models.ImageField(upload_to='rentas')

class Reservacion(models.Model):
    fecha_entrada = models.DateField(verbose_name="Fecha de entrada")
    fecha_salida = models.DateField(verbose_name="Fecha de salida")
    nombre_cliente = models.TextField(max_length=150,verbose_name="Nombre del cliente")
    email_cliente = models.EmailField(verbose_name="Correo electrónico")
    cantidad_personas = models.IntegerField(verbose_name="Cantidad de personas")
    verificado = models.BooleanField(default=False)
    confirmado = models.BooleanField(default=False)
    renta = models.ForeignKey(Renta)

    class Meta:
        verbose_name_plural ="Reservaciones"

class Comentarios(models.Model):
    nombre = models.TextField(max_length=150)
    fecha = models.DateField()
    comentario = models.TextField()
    renta = models.ForeignKey(Renta)

    class Meta:
        verbose_name_plural = "Comentarios"
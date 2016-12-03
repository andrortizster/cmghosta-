from django.contrib import admin
from .models import Provincia,Municipio,Renta,Galeria,Servicio,Reservacion,Comentarios

# Register your models here.
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class RentaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('imagen',)

class ReservacionAdmin(admin.ModelAdmin):
    list_display = ('fecha_entrada','fecha_salida','nombre_cliente')

class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Provincia,ProvinciaAdmin)
admin.site.register(Municipio,MunicipioAdmin)
admin.site.register(Servicio,ServicioAdmin)
admin.site.register(Renta,RentaAdmin)
admin.site.register(Galeria,GaleriaAdmin)
admin.site.register(Reservacion,ReservacionAdmin)
admin.site.register(Comentarios,ComentariosAdmin)
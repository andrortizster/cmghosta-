from django.contrib import admin
from .models import Provincia,Municipio,Renta,Galeria,Servicio,Reservacion,Comentarios,Mes

# Register your models here.
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

class RentaAdmin(admin.ModelAdmin):
    list_display = ('nombre','propietario',)
    filter_horizontal = ('meses_ta','servicio',)
    raw_id_fields = ('municipio',)
    search_fields = ('nombre',)

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('renta','imagen',)
    raw_id_fields = ('renta',)

class ReservacionAdmin(admin.ModelAdmin):
    list_display = ('fecha_entrada','fecha_salida','nombre_cliente')

class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

"""class MesAdmin(admin.ModelAdmin):
    list_display = ('nombre',)"""

admin.site.register(Provincia,ProvinciaAdmin)
admin.site.register(Municipio,MunicipioAdmin)
admin.site.register(Servicio,ServicioAdmin)
admin.site.register(Renta,RentaAdmin)
admin.site.register(Galeria,GaleriaAdmin)
admin.site.register(Reservacion,ReservacionAdmin)
admin.site.register(Comentarios,ComentariosAdmin)
admin.site.register(Mes)
#admin.site.register(Mes,MesAdmin)
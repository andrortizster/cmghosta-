from django.conf.urls import url
from . import views

app_name = 'rentas'
urlpatterns = [
    url(r'^ultimas/$',views.ultimas),
    url(r'^detalles/(\d+)/$',views.detalles),
    url(r'^confirmacion/(.+)/$',views.confirmacion),
    url(r'^verificacion/$',views.verificacion),
    url(r'^verificado/(\d+)/$',views.verificado),
    url(r'^lista/$',views.rentas_list),
    url(r'^encuentra_municipios/$', views.encuentra_municipios, name='encuentra_municipios'),
    url(r'^verificar/(.+)/$',views.verificar),
]
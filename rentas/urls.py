from django.conf.urls import url
from . import views

app_name = 'rentas'
urlpatterns = [
    url(r'^ultimas/$',views.ultimas),
    url(r'^detalles/(\d+)/$',views.detalles),
    url(r'^lista/$',views.rentas_list),
    url(r'^encuentra_municipios/$', views.encuentra_municipios, name='encuentra_municipios'),
]
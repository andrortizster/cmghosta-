from django.conf.urls import url
from . import views

app_name = 'rentas'
urlpatterns = [
    url(r'^ultimas/$',views.ultimas),
    url(r'^detalles/(\d+)/$',views.detalles),
]
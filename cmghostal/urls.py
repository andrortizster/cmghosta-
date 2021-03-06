"""cmghostal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from cmghostal.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles import views
from django.contrib.auth.views import login,logout
from . import views as cmgviews

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^accounts/login/$', login, {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', logout),
    url(r'^$', raiz),
    url(r'^contacto/$', cmgviews.contacto),
    url(r'^registro/$',registro),
    url(r'^admin/', admin.site.urls),
    url(r'^rentas/', include('rentas.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
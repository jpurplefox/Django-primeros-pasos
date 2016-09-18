"""primeros_pasos URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from mi_app.views import HomeView
from bandas import views as bandas_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^bandas/$', bandas_views.BandaList.as_view(), name='banda-list'),
    url(r'^bandas/(?P<pk>[0-9]+)/$', bandas_views.BandaDetail.as_view(), name='banda-detail'),
    url(r'^bandas/crear/$', bandas_views.BandaCreate.as_view(), name='banda-create'),
    url(r'^bandas/(?P<pk>[0-9]+)/modificar/$', bandas_views.BandaUpdate.as_view(), name='banda-update'),
    url(r'^bandas/(?P<pk>[0-9]+)/eliminar/$', bandas_views.BandaDelete.as_view(), name='banda-delete'),
]

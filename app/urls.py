from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import path, re_path


urlpatterns = [
    path('', views.index),
    path('iniciosesion/', views.iniciosesion),
    path('cerrarsesion/', views.cerrarsesion),
    path('secretaria/', views.secretaria),
    path('docencia/', views.docentes),
    path('vinculacion/', views.vinculacion),
    path('investigacion/', views.investigacion),
    path('laboratorio/', views.laboratorio),
    path('docentes/', views.docentes),
    path('avisos/', views.avisos),
    path('subir_documentos/', views.subir_documentos),

    
    
]

from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse, HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
from django.core.mail import EmailMessage
from django.conf import settings
from django.core import serializers
from django.contrib.auth.hashers import check_password
import json
import smtplib
import sweetify
import datetime

# Create your views here.

#
def index(request):
    usuario = request.user
    if usuario.is_active:
        return render (request, 'index.html', {})
    else:
        return render(request, 'login.html',{})



# LOGIN Y CERRAR SESION
def iniciosesion(request):
    username = request.POST.get("usuario")
    password = request.POST.get("password")
    print("Esto llego: ", username)
    try: 
        username = authenticate(request, username=username, password=password)
        login(request,username)
        return redirect('/')
    except Exception as e:
        sweetify.error(request, 'Oops!', text='¡El Usuario y/o Contraseña es Incorrecto!', persistent=':´(')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def cerrarsesion(request):
	logout(request)
	return HttpResponseRedirect("/")

def secretaria(request):

    return render(request, 'secretaria.html', {})

def docencia(request):

    return render(request, 'docencia.html', {})

def vinculacion(request):

    return render(request, 'vinculacion.html', {})

def investigacion(request):

    return render(request, 'investigacion.html', {})

def laboratorio(request):

    return render(request, 'laboratorio.html', {})

def docentes(request):

    return render(request, 'docentes.html', {})

def avisos(request):
    usuario = request.user
    usuarios = Usuarios.objects.get(usuario=usuario)
    usuario_establecido = usuarios.tipo
    print("tipo de usuario: ", usuario_establecido)
    all_user = Usuarios.objects.all()

    comunicados = Comunicados.objects.all()
    comunicados_secretaria = Mi_comunicado.objects.filter(usuario__tipo= usuario_establecido)
    print("mis comuniocados_: ", comunicados_secretaria)
   

    

    datos = {"comunicados":comunicados, "usuario":usuario_establecido,"all_user":all_user,
    "comunicados_secretaria":comunicados_secretaria}

    return render(request, 'avisos.html', datos)


#vistas para comunicados
def subir_documentos(request):
    usuarios = request.POST.getlist("usuario")
    titulo = request.POST.get("titulo")
    descripcion = request.POST.get("descripcion")
    documento = request.POST.get("documento")
    imagen = request.POST.get("imagen")
    link = request.POST.get("link")

    comunicado = Comunicados.objects.create(titulo=titulo, descripcion=descripcion, documento=documento,
    imagen=imagen, link=link)

    for b in usuarios:
        c = Usuarios.objects.get(tipo=b)
        mi_comunicado = Mi_comunicado.objects.create(usuario=c, comunicado=comunicado)


    print("Objeto creado con exito")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))



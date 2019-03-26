from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from urllib import parse

# Create your views here.

#----------------------------------------------------------------
					#MAIN VIEW
#----------------------------------------------------------------

def index (request):
	context = {}
	return render (request,"index.html")


#----------------------------------------------------------------
					#Inicio de sesión y registro
#----------------------------------------------------------------

def init_sesion (request):
	context = {}
	return render (request, "initsesion.html")


def registro (request):
	context = {}
	return render (request, "registro.html")



#----------------------------------------------------------------
					#Panel Dra.
#----------------------------------------------------------------

def dra (request):
	lista = "bitch"
	context = {"lista": lista}
	return render (request, "init_doctora.html")



#----------------------------------------------------------------
					#Panel Paciente.
#----------------------------------------------------------------

def paciente (request):
	context = {}
	return render (request, "init_paciente.html")


def paciente_solicitar (request):
	context = {}
	return render (request, "solicitar_cita.html")



def perfil (request):
	context = {}
	return render (request, "perfil.html")
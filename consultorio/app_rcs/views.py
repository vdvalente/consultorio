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


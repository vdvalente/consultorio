from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #/, /inicio
    path("", views.index, name="index_"), 
    path("index/", views.index, name="index"),


    #/login  
    path("login/", views.init_sesion, name="login" ),

   #/registro y perfil
    path("registro/",views.registro, name="registro" ),
    path("perfil/",views.perfil, name="perfil" ),


 #Acomodar las vistas luego, de forma que se envie y reciba la info correspondiente# --> @If => user.type:(p1||p2)
    #/usuarios
    path("paciente/",views.paciente, name="paciente" ),
    path("paciente/solicitar-cita",views.paciente_solicitar, name="paciente_"),
    path("dra/",views.dra, name="dra" ),

   
   



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
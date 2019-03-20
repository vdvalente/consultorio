from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #/, /inicio
    path("", views.index, name="index_"), 
    path("inicio/", views.index, name="index"),

   

    #/lenguajes, lenguajes/c-->   <str:lenguaje>  
   # path("lenguajes/", views.lenguajes_main, name="inicio_lenguajes" ),
   # path("lenguajes/<str:lenguaje>/", views.lenguajes_detail, name="lenguajes_det"),

 										#EJEMPLOS: 
 				#/librerias, librerias/c/ ---> librerias/<str:lenguaje>/
 			#librerias/c/sdl --> librerias/<str:lenguaje>/<str:libreria>/
   
   # path("librerias/",views.librerias_main, name="librerias" ),
   # path("librerias/<str:lenguaje>/", views.librerias_overview, name="librerias_over" ),
    #path("librerias/<str:lenguaje>/<str:libreria>/",views.librerias_detail, name="librerias_det" ),


    #/frameworks, frameworks/c/allegro -->   <str:lenguaje>/<str:framework>
    #path("frameworks/",views.frameworks_main, name="frameworks" ), 
    #path("frameworks/<str:lenguaje>/",views.frameworks_overview, name="frameworks_over"),
    #path("frameworks/<str:lenguaje>/<str:framework>/",views.framework_detail, name="frameworks_det"),

    #path("login", views.login , name="login"), """

]

#if settings.DEBUG:
 #   urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
  #  urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
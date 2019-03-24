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

   #/registro
    path("registro/",views.registro, name="registro" ),
   

    #/frameworks, frameworks/c/allegro -->   <str:lenguaje>/<str:framework>
    #path("frameworks/",views.frameworks_main, name="frameworks" ), 
    #path("frameworks/<str:lenguaje>/",views.frameworks_overview, name="frameworks_over"),
    #path("frameworks/<str:lenguaje>/<str:framework>/",views.framework_detail, name="frameworks_det"),

    #path("login", views.login , name="login"), """

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
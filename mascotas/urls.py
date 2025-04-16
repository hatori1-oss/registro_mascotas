from django.urls import path
from mascotas.views import registrar_usuario, lista_mascotas
from . import views

urlpatterns = [
    path('login_usuario/', views.login_usuario, name='login'),
    #path('registrar_usuario/', registrar_usuario, name='registrar_usuario'),
    path('lista/', lista_mascotas, name='lista_mascotas'),
    path('',views.index,name = 'index'),
    #path('consultar/', views.consultar_mascotas, name = 'consultar_mascotas'),
    #path('mascota/<uuid:uuid>', views.consultar_mascotas, name = 'consultar_mascotas'),
    path('consultar_mascotas/', views.consultar_mascotas, name = 'consultar_mascotas'),
    path('registro/',views.registro,name='registro'),
    path('registro_exitoso/',views.registro_exitoso,name='registro_exitoso'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_cliente, name='lista_cliente'),
    path('agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('<int:pk>/', views.detalle_cliente, name='detalle_cliente'),
    path('<int:pk>/editar/', views.editar_cliente, name='editar_cliente'),
    path('<int:pk>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),
]

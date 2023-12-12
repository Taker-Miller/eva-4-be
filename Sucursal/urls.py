from django.urls import path
from . import views

urlpatterns = [
    path('sucursal/', views.lista_sucursal, name='lista_sucursal'),
    path('sucursal/agregar/', views.agregar_sucursal, name='agregar_sucursal'),
    path('sucursal/<int:pk>/', views.detalle_sucursal, name='detalle_sucursal'),
    path('sucursal/<int:pk>/editar/', views.editar_sucursal, name='editar_sucursal'),
    path('sucursal/<int:pk>/eliminar/', views.eliminar_sucursal, name='eliminar_sucursal'),
]

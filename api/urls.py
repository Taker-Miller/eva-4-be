from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AutoViewSet, ClienteViewSet, SucursalViewSet

router = DefaultRouter()
router.register(r'autos', AutoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'sucursales', SucursalViewSet)

# Usa router.urls para incluir las URLs creadas por el DefaultRouter
urlpatterns = [
    path('', include(router.urls)),
]

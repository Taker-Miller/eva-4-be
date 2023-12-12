
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from api.views import AutoViewSet, ClienteViewSet, SucursalViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'autos', AutoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'sucursales', SucursalViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('autos/', include('Auto.urls')),
    path('clientes/', include('Cliente.urls')),
    path('sucursales/', include('Sucursal.urls')),
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(url='autos/', permanent=True)),  
]

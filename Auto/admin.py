from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from .models import Auto, Cliente
from django.utils.html import format_html
from django.urls import reverse

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ['patente', 'marca', 'color', 'modelo', 'precio', 'numero_de_ruedas', 'Propietario', 'sucursal', 'acciones']
    def acciones(self, obj):
        return format_html(
            '<a class="button" href="{}">Editar</a>&nbsp;'
            '<a class="button" href="{}">Eliminar</a>',
            reverse('admin:Auto_auto_change', args=[obj.pk]),  
            reverse('admin:Auto_auto_delete', args=[obj.pk]),  
        )
    acciones.short_description = 'Acciones'
    acciones.allow_tags = True

    def Propietario(self, obj):
        return obj.propietario.nombre  
    Propietario.short_description = 'Propietario'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:object_id>/eliminar/',
                self.admin_site.admin_view(self.process_eliminar),
                name='Auto_auto_delete',
            ),
        ]
        return custom_urls + urls

    def process_eliminar(self, request, object_id):
        obj = self.get_object(request, object_id)
        if obj:
            obj.delete()
            self.message_user(request, f'El auto {obj} ha sido eliminado.')
        return HttpResponseRedirect("../")
admin.site.register(Cliente)
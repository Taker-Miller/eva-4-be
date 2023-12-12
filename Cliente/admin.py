from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from .models import Cliente
from django.utils.html import format_html
from django.urls import reverse

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email', 'telefono', 'direccion', 'fecha_de_nacimiento', 'acciones']

    def acciones(self, obj):
        return format_html(
            '<a class="button" href="{}">Editar</a>&nbsp;'
            '<a class="button" href="{}">Eliminar</a>',
            reverse('admin:Cliente_cliente_change', args=[obj.pk]),
            reverse('admin:Cliente_cliente_delete', args=[obj.pk]),

    )

    acciones.short_description = 'Acciones'
    acciones.allow_tags = True

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:object_id>/eliminar/',
                self.admin_site.admin_view(self.process_eliminar),
                name='app_cliente_delete',
            ),
        ]
        return custom_urls + urls

    def process_eliminar(self, request, object_id):
        obj = self.get_object(request, object_id)
        if obj:
            obj.delete()
            self.message_user(request, f'El cliente {obj} ha sido eliminado.')
        return HttpResponseRedirect("../")

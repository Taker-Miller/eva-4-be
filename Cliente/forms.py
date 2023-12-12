from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Cliente
import datetime
import re

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono', 'direccion', 'fecha_de_nacimiento']
        widgets = {
            'fecha_de_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError('Ingrese un correo electrónico válido.')

        if Cliente.objects.filter(email=email).exists():
            raise ValidationError('Este correo electrónico ya está registrado.')
        return email

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if not re.match(r'^\d+$', telefono):
            raise ValidationError('El número de teléfono debe contener solo números.')
        return telefono

    def clean_fecha_de_nacimiento(self):
        fecha_de_nacimiento = self.cleaned_data['fecha_de_nacimiento']
        hoy = datetime.date.today()
        if fecha_de_nacimiento > hoy:
            raise ValidationError('La fecha de nacimiento no puede ser en el futuro.')

        edad = hoy.year - fecha_de_nacimiento.year - ((hoy.month, hoy.day) < (fecha_de_nacimiento.month, fecha_de_nacimiento.day))
        if edad < 18:
            raise ValidationError('Debes tener al menos 18 años para registrarte.')
        return fecha_de_nacimiento

   

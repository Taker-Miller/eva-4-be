from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Sucursal
import datetime
import re

class SucursalForm(forms.ModelForm):

    class Meta:
        model = Sucursal
        fields = ['nombre', 'direccion', 'apertura', 'gerente', 'fono', 'correo']
        widgets = {
            'apertura': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_correo(self):
        correo = self.cleaned_data['correo']
        try:
            validate_email(correo)
        except ValidationError:
            raise ValidationError('Ingrese un correo electrónico válido.')

        if Sucursal.objects.filter(correo=correo).exists():
            raise ValidationError('Este correo electrónico ya está registrado.')
        return correo

    def clean_fono(self):
        fono = self.cleaned_data['fono']
        if not re.match(r'^\d+$', fono):
            raise ValidationError('El número de teléfono debe contener solo números.')
        return fono

    def clean_apertura(self):
        apertura = self.cleaned_data['apertura']
        hoy = datetime.date.today()
        if apertura > hoy:
            raise ValidationError('La fecha de apertura no puede ser en el futuro.')
        return apertura

from django import forms
from django.core.exceptions import ValidationError
from .models import Auto

class AutoForm(forms.ModelForm):
    
    def clean_numero_de_ruedas(self):
        numero_de_ruedas = self.cleaned_data['numero_de_ruedas']
        if numero_de_ruedas <= 1 or numero_de_ruedas > 4:
            raise ValidationError('Número de ruedas inválido. Debe ser entre 1 y 4.')
        return numero_de_ruedas

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio <= 0:
            raise ValidationError('El precio debe ser mayor que cero.')
        return precio

    def clean_patente(self):
        patente = self.cleaned_data['patente']
        if not patente.isalnum():
            raise ValidationError('La patente debe contener solo caracteres alfanuméricos.')
        return patente

    def clean_marca(self):
        marca = self.cleaned_data['marca']
        if not marca.isalpha():
            raise ValidationError('La marca debe contener solo letras.')
        return marca

    def clean_color(self):
        color = self.cleaned_data['color']
        if not color.isalpha():
            raise ValidationError('El color debe contener solo letras.')
        return color

    def clean_modelo(self):
        modelo = self.cleaned_data['modelo']
        if not modelo.isalnum():
            raise ValidationError('El modelo debe contener solo caracteres alfanuméricos.')
        return modelo

    class Meta:
        model = Auto
        fields = ['patente', 'marca', 'color', 'modelo', 'precio', 'numero_de_ruedas', 'propietario']

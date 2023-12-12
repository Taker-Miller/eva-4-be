from rest_framework import serializers
from .models import Auto, Sucursal, Cliente

class AutoSerializer(serializers.ModelSerializer):
    sucursal = serializers.SlugRelatedField(
        queryset=Sucursal.objects.all(),
        slug_field='nombre'
    )
    propietario = serializers.SlugRelatedField(
        queryset=Cliente.objects.all(),
        slug_field='nombre',  
    )

    class Meta:
        model = Auto
        fields = '__all__'

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

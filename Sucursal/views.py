from django.shortcuts import render, get_object_or_404, redirect
from .models import Sucursal
from .forms import SucursalForm

def home_view(request):
    return render(request, 'home.html', {})

def lista_sucursal(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursal/lista_sucursal.html', {'sucursales': sucursales})

def detalle_sucursal(request, pk):
    sucursal = get_object_or_404(Sucursal, pk=pk)
    return render(request, 'sucursal/detalle_sucursal.html', {'sucursal': sucursal})

def agregar_sucursal(request):
    if request.method == 'POST':
        form = SucursalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_sucursal')
    else:
        form = SucursalForm()
    return render(request, 'sucursal/agregar_sucursal.html', {'form': form})

def editar_sucursal(request, pk):
    sucursal = get_object_or_404(Sucursal, pk=pk)
    if request.method == 'POST':
        form = SucursalForm(request.POST, instance=sucursal)
        if form.is_valid():
            form.save()
            return redirect('detalle_sucursal', pk=sucursal.pk)
    else:
        form = SucursalForm(instance=sucursal)
    return render(request, 'sucursal/editar_sucursal.html', {'form': form})

def eliminar_sucursal(request, pk):
    sucursal = get_object_or_404(Sucursal, pk=pk)
    if request.method == 'POST':
        sucursal.delete()
        return redirect('lista_sucursal')
    return render(request, 'sucursal/eliminar_sucursal.html', {'sucursal': sucursal})

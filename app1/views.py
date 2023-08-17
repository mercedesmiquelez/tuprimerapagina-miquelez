from django.shortcuts import render, redirect

from .models import Producto
from .forms import Comprador_forms, Vendedor_forms, Producto_forms, UsuSearchForm

# Create your views here.


def comprador(request):
    if request.method == 'POST':
        comprador_formulario = Comprador_forms(request.POST)
        
        if comprador_formulario.is_valid:
            comprador_formulario.save()
            
            return redirect('/app1/')
    else:
        comprador_formulario = Comprador_forms()

    return render(request, 'comprador.html',{"comprador_formulario": comprador_formulario})


def vendedor(request):
    if request.method == 'POST':
        vendedor_formulario = Vendedor_forms(request.POST)
        
        if vendedor_formulario.is_valid:
            vendedor_formulario.save()
            
            return redirect('/app1/')
    else:
        vendedor_formulario = Vendedor_forms()
    
    
    return render(request, 'vendedor.html',{"vendedor_formulario": vendedor_formulario})


def producto(request):
    if request.method == 'POST':
        producto_formulario = Producto_forms(request.POST)
        
        if producto_formulario.is_valid():
            producto_formulario.save()       
            return redirect('/app1/')
    else:
        producto_formulario = Producto_forms()
    
    return render(request, 'producto.html',{"producto_formulario": producto_formulario})


def inicio(request):
    return render(request,'inicio.html')


def buscarProductos(request):
    productos = []
    form = UsuSearchForm(request.GET)

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')

        # Realizar la búsqueda en el modelo Producto por nombre
        if nombre:
            productos= Producto.objects.filter(nombre__icontains=nombre)

    return render(request, 'buscarproducto.html', {'form': form, 'productos': productos})

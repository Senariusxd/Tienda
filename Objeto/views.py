from django.shortcuts import render, redirect, get_object_or_404
from .models import Generos, Producto
from .forms import GenerosForm, ProductoForm  # Asegúrate de crear este formulario

def home(request):
    return render(request, 'home.html')

def lista_generos(request):
    generos = Generos.objects.all()
    return render(request, 'lista_generos.html', {'generos': generos})

def crear_generos(request):
    if request.method == 'POST':
        form = GenerosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_generos')
    else:
        form = GenerosForm()
    return render(request, 'crear_generos.html', {'form': form})

def editar_generos(request, pk):
    genero = get_object_or_404(Generos, pk=pk)
    if request.method == 'POST':
        form = GenerosForm(request.POST, instance=genero)
        if form.is_valid():
            form.save()
            return redirect('lista_generos')
    else:
        form = GenerosForm(instance=genero)
    return render(request, 'crear_generos.html', {'form': form})

def eliminar_generos(request, pk):
    genero = get_object_or_404(Generos, pk=pk)
    if request.method == 'POST':
        genero.delete()
        return redirect('lista_generos')
    return render(request, 'eliminar_genero.html', {'genero': genero})




def lista_productos(request, genero_id):
    genero = get_object_or_404(Generos, pk=genero_id)
    productos = genero.productos.all()
    return render(request, 'lista_productos.html', {'productos': productos, 'genero': genero})

def crear_productos(request, genero_id):
    genero = get_object_or_404(Generos, pk=genero_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.generos = genero
            producto.save()
            return redirect('lista_productos', genero_id=genero.id)
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form, 'genero': genero})

def editar_productos(request, genero_id, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos', genero_id=genero_id)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'genero': producto.generos})

def eliminar_productos(request, genero_id, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos', genero_id=genero_id)
    return render(request, 'eliminar_producto.html', {'producto': producto, 'genero': producto.generos})
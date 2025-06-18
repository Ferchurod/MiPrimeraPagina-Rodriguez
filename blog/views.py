from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, PostForm
from .models import Post

# Vista para crear un autor
def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_autor')  # Redirige a la misma página después de guardar
    else:
        form = AutorForm()
    return render(request, 'crear_autor.html', {'form': form})

# Vista para crear una categoría
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_categoria')
    else:
        form = CategoriaForm()
    return render(request, 'crear_categoria.html', {'form': form})

# Vista para crear un post
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_post')
    else:
        form = PostForm()
    return render(request, 'crear_post.html', {'form': form})

# Vista para buscar posts
def buscar_post(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(titulo__icontains=query) if query else Post.objects.all()
    return render(request, 'buscar_post.html', {'posts': posts})

def inicio(request):
    return render(request, 'inicio.html')

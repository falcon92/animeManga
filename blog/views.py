from django.shortcuts import render, get_object_or_404
from .models import Producto, Anime
from django.utils import timezone
from django.db.models import Q
#from django.http import HttpResponse
#import json

def principal(request):
    productos = Producto.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    animes = Anime.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    query = request.GET.get("q")
    if query:
        animes = animes.filter(
        Q(nombre__icontains=query) |
        Q(descripcion__icontains=query) |
        Q(autor__icontains=query)
        ).distinct()
    return render(request, 'blog/principal.html', {'productos': productos, 'animes' : animes})


def producto_detail(request, pk):
    p = get_object_or_404(Producto, pk=pk)
    return render(request, 'blog/producto_detail.html', {'p': p})

def mangas(request):
    productos = Producto.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/mangas.html', {'productos': productos})

def animes(request):
    animes = Anime.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/animes.html', {'animes' : animes})

def anime_detail(request, pk):
    m = get_object_or_404(Anime, pk=pk)
    return render(request, 'blog/anime_detail.html', {'m' : m})

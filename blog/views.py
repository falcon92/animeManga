from django.shortcuts import render, get_object_or_404
from .models import Producto
from django.utils import timezone

def principal(request):
    productos = Producto.objects.filter(fecha_inicio__lte=timezone.now()).order_by('fecha_inicio')
    return render(request, 'blog/principal.html', {'productos': productos})


def producto_detail(request, pk):
    p = get_object_or_404(Producto, pk=pk)
    return render(request, 'blog/producto_detail.html', {'p': p})

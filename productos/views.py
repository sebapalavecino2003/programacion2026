from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import CategoriaProducto, Producto
from .serializers import CategoriaProductoSerializer, ProductoSerializer


class CategoriaProductoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nombre']
    ordering_fields = ['id', 'nombre']
    ordering = ['nombre']


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.select_related('categoria').all()
    serializer_class = ProductoSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['codigo', 'nombre', 'categoria__nombre']
    ordering_fields = ['id', 'codigo', 'nombre', 'precio_venta', 'creado_en']
    ordering = ['nombre']
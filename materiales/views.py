from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import CategoriaMaterial, Material
from .serializers import CategoriaMaterialSerializer, MaterialSerializer


class CategoriaMaterialViewSet(viewsets.ModelViewSet):
    queryset = CategoriaMaterial.objects.all()
    serializer_class = CategoriaMaterialSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["nombre"]
    ordering_fields = ["id", "nombre"]
    ordering = ["nombre"]


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.select_related("categoria").all()
    serializer_class = MaterialSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["codigo", "nombre", "categoria__nombre"]
    ordering_fields = ["id", "codigo", "nombre", "costo_referencia", "creado_en"]
    ordering = ["nombre"]
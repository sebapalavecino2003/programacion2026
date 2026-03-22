from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('productos.urls')),
    path('api/', include('materiales.urls')),
    path('api/', include('recetas.urls')),
    path('api/', include('clientes.urls')),
    path('api/', include('proveedores.urls')),

]
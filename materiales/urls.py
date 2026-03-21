from rest_framework.routers import DefaultRouter
from .views import CategoriaMaterialViewSet, MaterialViewSet

router = DefaultRouter()
router.register(r"categorias-materiales", CategoriaMaterialViewSet, basename="categoria-material")
router.register(r"materiales", MaterialViewSet, basename="material")

urlpatterns = router.urls
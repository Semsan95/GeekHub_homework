from . import views
from rest_framework.routers import DefaultRouter

app_name = "api"

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'cart', views.CartViewSet, basename='cart')

urlpatterns = router.urls
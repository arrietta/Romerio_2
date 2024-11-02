from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static
from romerio import views

router = DefaultRouter()
router.register(r'doors', views.ShapeViewSet)
router.register(r'collections', views.CollectionViewSet)
router.register(r'toCart', views.DoorViewSet)
router.register(r'cart', views.CartViewSet,basename="CartApi")
router.register(r'order', views.OrderViewSet,basename="OrderApi")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/csrf/', views.get_csrf_token, name='get_csrf_token'),
    path('', views.Main, name='main'),
    path('catalog', views.catalog, name='catalog'),
    path('catalog/<int:id>', views.catalog_element, name='Constructor'),

    path('cart', views.cart, name='cart'),
    path('api/v1/door/<int:shape_id>', views.DoorDetailView.as_view(), name='door'),
    path('privacy', views.privacy, name='privacy'),
    path('api/identification', views.identification, name='identification'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

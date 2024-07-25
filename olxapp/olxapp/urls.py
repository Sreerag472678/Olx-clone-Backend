from django.contrib import admin
from django.urls import path,include
from olx import views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings 
from olx.views import product_list,search_products, get_profile,ProductViewListAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/upload/', ProductViewListAPIView.as_view(), name='product-create'),
    path('product_view/', product_list),
    path('products/search/', search_products, name='product-search'),
    path('api/profile/', get_profile, name='get_profile'),
    path('api/', include('olx.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
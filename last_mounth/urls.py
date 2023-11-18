from django.contrib import admin
from django.urls import path, include
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', include('product.urls')),
    path('api/v1/products/', include('product.urls')),
    path('api/v1//reviews/', include('product.urls')),
    path('products/products/reviews/', include('product.urls')),
    path('api/v1/accounts/', include('accounts.urls'))
]

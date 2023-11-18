from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.product_list_api_view),
    path('<int:id>/', views.product_detail_api_view),
    path('', views.category_list_api_view),
    path('<int:id>/', views.category_detail_api_view),
    path('', views.review_list_api_view),
    path('<int:id>/', views.review_detail_api_view),
]
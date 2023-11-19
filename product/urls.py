from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.product_list_api_view),
    path('<int:id>/', views.product_detail_api_view),
    path('products/', views.ProductListCreateAPIView.as_view()),
    path('products/<int:id>/', views.ProductListCreateAPIView.as_view()),
    path('', views.category_list_api_view),
    path('<int:id>/', views.category_detail_api_view),
    path('category/', views.CategoryListCreateAPIView.as_view()),
    path('category/<int:id>/', views.CategoryListCreateAPIView.as_view()),
    path('', views.review_list_api_view),
    path('<int:id>/', views.review_detail_api_view),
    path('review/', views.ReviewListCreateAPIView.as_view()),
    path('review/<int:id>/', views.ReviewListCreateAPIView.as_view()),
]
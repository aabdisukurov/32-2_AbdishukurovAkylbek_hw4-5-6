from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from django.views import generic
from product.models import Product, Category, Review
from product.serializers import ProductSerializers, CategorySerializers, ReviewSerializers, ProductReviewSerializers


@api_view(["GET", "POST"])
def product_list_api_view(request):
    if request.method == "GET":
        queryset = Product.objects.all()
        serializer = ProductSerializers(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = ProductSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def product_detail_api_view(request, id):
    try:
        queryset = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ProductSerializers(queryset)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = ProductSerializers(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return  Response(serializer.data, status.HTTP_200_OK)
    elif request.method == "DELETE":
        queryset.delete()
        return Response(status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def category_list_api_view(request):
    if request.method == "GET":
        queryset = Category.objects.all()
        serializer = CategorySerializers(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = CategorySerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def category_detail_api_view(request, id):
    try:
        queryset = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = CategorySerializers(queryset)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = CategorySerializers(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == "DELETE":
        queryset.delete()
        return Response(status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def review_list_api_view(request):
    if request.method == "GET":
        queryset = Review.objects.all()
        serializer = ReviewSerializers(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = ReviewSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def review_detail_api_view(request, id):
    try:
        queryset = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ReviewSerializers(queryset)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = ReviewSerializers(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == "DELETE":
        queryset.delete()
        return Response(status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
def product_review_list_api_view(request):
    queryset = Product.objects.all()
    serializer = gitProductReviewSerializers(queryset, many=True)
    return  Response(serializer.data, status.HTTP_200_OK)
from django.db import transaction
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from django.views import generic
from product.models import Product, Category, Review
from product.serializers import ProductSerializers, CategorySerializers, ReviewSerializers, ProductReviewSerializers, ProductCreateValidateSerializer


@api_view(["GET", "POST"])
def product_list_api_view(request):
    if request.method == "GET":
        products = Product.objects.select_related('category').all()
        products_json = ProductSerializers(products, many=True).data
        return Response(data=products_json)
    elif request.method == "POST":
        with transaction.atomic():
            serializer = ProductCreateValidateSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(status=status.HTTP_400_BAD_REQUEST)
            title = request.data.get('title')
            category = request.data.get('category')
            description = request.data.get('description')
            price = request.data.get('price')
            product = Product.objects.create(title=title, description=description, price=price, category=category)
            return Response(status= status.HTTP_201_CREATED,
                            data={'id': product.id, 'title': product.title})


@api_view(["GET", "PUT", "DELETE"])
def product_detail_api_view(request, product_id):
    try:
        product = Product.objects.select_related('category').get(id=product_id)
    except Product.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        product_json = ProductSerializers(product, many=False).data
        return Response(data=product_json)
    elif request.method == "PUT":
        serializer = ProductCreateValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        product.title = request.data.get('title')
        product.category = request.data.get('category')
        product.description = request.data.get('description')
        product.price = request.data.get('price')
        return Response(status= status.HTTP_200_OK)
    elif request.method == "DELETE":
        product.delete()
        return Response(status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def category_list_api_view(request):
    if request.method == "GET":
        category = Category.objects.select_related('name').all()
        category_json = CategorySerializers(category, many=True).data
        return Response(data=category_json)
    elif request.method == "POST":
        with transaction.atomic():
            serializer = ProductCreateValidateSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(status=status.HTTP_400_BAD_REQUEST)
            name = request.data.get('name')
            category = Product.objects.create(name=name)
            return Response(status=status.HTTP_201_CREATED,
                            data={'id': category.id, 'title': category.title})


@api_view(["GET", "PUT", "DELETE"])
def category_detail_api_view(request, category_id):
    try:
        category = Category.objects.select_related('name').get(id=category_id)
    except Category.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        category_json = CategorySerializers(category, many=False).data
        return Response(data=category_json)
    elif request.method == "PUT":
        serializer = ProductCreateValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        category.name = request.data.get('name')
        return Response(status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        category.delete()
        return Response(status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def review_list_api_view(request):
    if request.method == "GET":
        review = Review.objects.select_related('product').all()
        review_json = ReviewSerializers(review, many=True).data
        return Response(data=review_json)
    elif request.method == "POST":
        with transaction.atomic():
            serializer = ProductCreateValidateSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(status=status.HTTP_400_BAD_REQUEST)
            text = request.data.get('text')
            product = request.data.get('product')
            stars = request.data.get('stars')
            review = Product.objects.create(text=text, product=product, stars=stars)
            return Response(status=status.HTTP_201_CREATED,
                            data={'id': review.id, 'title': review.title})


@api_view(["GET", "PUT", "DELETE"])
def review_detail_api_view(request, review_id):
    try:
        review = Review.objects.select_related('product').get(id=review_id)
    except Review.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        review_json = ReviewSerializers(review, many=False).data
        return Response(data=review_json)
    elif request.method == "PUT":
        serializer = ProductCreateValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        review.text = request.data.get('text')
        review.product = request.data.get('product')
        review.stars = request.data.get('stars')
        return Response(status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        review.delete()
        return Response(status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def product_review_list_api_view(request):
    queryset = Product.objects.all()
    serializer = ProductReviewSerializers(queryset, many=True)
    return Response(serializer.data, status.HTTP_200_OK)
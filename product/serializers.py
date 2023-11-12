from rest_framework import serializers
from .models import Category, Product, Review

class CategorySerializers(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = '__all__'
    def get_products_count(self, obj):
        return obj.products.count()


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductReviewSerializers(serializers.ModelSerializer):
    reviews = ReviewSerializers(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'

    def  get_average_rating(self, obj):
        total_stars = sum(review.stars for review in obj.reviews.all())
        num_reviews = obj.reviews.count()
        if num_reviews > 0:
            return total_stars / num_reviews
        else:
            return 0.0
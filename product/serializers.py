from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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

class ProductCreateValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, min_length=3, max_length=50)
    description = serializers.CharField(required=False)
    price = serializers.IntegerField(default=0)
    category = serializers.ListField(child=serializers.IntegerField())

    def validate_category(self, category):
        for category_id in category:
            try:
                Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                raise ValidationError('Category does not exist')
        return category


from django.db import models

STARS = [
    (1, '1 звезда'),
    (2, '2 звезды'),
    (3, '3 звезды'),
    (4, '4 звезды'),
    (5, '5 звезд')
]

class Category(models.Model):
    name = models.CharField("Укажите название категории:", max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField("Укажите название продукта:", max_length=100)
    description = models.TextField("Укажите описание продукта:", blank=True, null=True)
    price = models.IntegerField("Укажите цену продукта:")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="product_category"
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.CharField("Укажите текст отзыва:", max_length=100)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="comment_product"
    )
    stars = models.PositiveIntegerField(choices=STARS, default=1)

    def __str__(self):
        return self.text

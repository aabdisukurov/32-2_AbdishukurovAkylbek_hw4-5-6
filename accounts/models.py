from django.db import models

# Create your models here.

class ConfirmCode(models.Model):
    code = models.IntegerField(max_length=6)

    def __str__(self):
        return self.code
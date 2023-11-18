from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

class SignupValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    code = serializers.IntegerField(0, )
    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exist!')

class LoginValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True, max_length=100)
    password = serializers.CharField(required=True, max_length=255)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=255)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=255)

    def create(self, validated_data):
        username = validated_data.email
        # User.objects.create_user(username, email=None, password=None, **extra_fields)
        validated_data

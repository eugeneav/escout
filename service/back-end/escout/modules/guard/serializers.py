import logging
from django.db import DatabaseError
from rest_framework import serializers
from django.contrib.auth.models import User

# Get an instance of a logger
logger = logging.getLogger(__name__)


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True, max_length=100)
    password = serializers.CharField(required=True, max_length=255)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=255)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=255)

    def create(self, validated_data):

        username = validated_data['email']
        email = validated_data['email']
        password = validated_data['password']
        # first_name = "" validated_data['first_name']
        # last_name = validated_data['last_name']

        try:
            User.objects.get(username=email)
            return {
                'status': 'user_exists'
            }
        except User.DoesNotExist:

            try:
                User.objects.create_user(username, email=email, password=password)
                return {
                    'status': 'user_created'
                }
            except DatabaseError as error:
                logger.error(error.message)
                return {
                    'status': 'user_create_error'
                }

import logging

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import DatabaseError
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

# Get an instance of a logger
from escout.guard.models import Account

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

        try:
            User.objects.get(username=email)
            return {
                'status': 'user_exists'
            }
        except User.DoesNotExist:

            try:
                user_model = User.objects.create_user(username, email=email, password=password)

                account_model = Account()
                account_model.owner = user_model
                account_model.title = ''
                account_model.description = ''
                account_model.save()

                return {
                    'status': 'user_created'
                }
            except DatabaseError as error:
                logger.error(error)
                return {
                    'status': 'user_create_error'
                }

    def update(self, instance, validated_data):
        pass

    # TODO
    def authenticate(self, validated_data):

        email = validated_data['email']
        password = validated_data['password']

        if email and password:
            user = authenticate(username=email, password=password)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg)

        return user

import uuid
import logging

from django.db import DatabaseError
from rest_framework import serializers
from escout.dashboard.models import Application

logger = logging.getLogger(__name__)


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(required=True, max_length=255)
    description = serializers.CharField(required=False)

    class Meta:
        model = Application
        fields = ('title', 'description')

    def create(self, validated_data):

        account = validated_data['account']
        personal_id = str(uuid.uuid1())
        title = validated_data['title']
        description = validated_data['description']

        try:
            application_model = Application.create(account, personal_id, title, description)
            return {
                'status': 'user_created',
                'application': {
                    'personal_id': personal_id
                }
            }
        except DatabaseError as error:
            logger.error(error)
            return {
                'status': 'user_create_error'
            }
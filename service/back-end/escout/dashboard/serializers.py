import uuid
import logging

from rest_framework import serializers
from escout.dashboard.models import Application
from escout.dashboard.models import Event

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

        Application.create(account, personal_id, title, description)
        return {
            'status': 'application_created',
            'application': {
                'personal_id': personal_id
            }
        }

    def update(self, application_model, validated_data):
        application_model.title = validated_data.get('title', application_model.title)
        application_model.description = validated_data.get('description', application_model.description)
        application_model.save()

        return {
            'status': 'application_updated'
        }


class EventSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(max_length=256)
    type = serializers.CharField(max_length=256)
    description = serializers.CharField(required=False)
    priority = serializers.IntegerField(required=False)
    user_session_id = serializers.IntegerField(required=False)
    user_timezone = serializers.IntegerField(required=False)
    start_time = serializers.IntegerField(required=False)
    stop_time = serializers.IntegerField(required=False)
    created = serializers.DateTimeField()

    class Meta:
        model = Event
        fields = (
            'name',
            'type',
            'description',
            'priority',
            'user_session_id',
            'user_timezone',
            'start_time',
            'stop_time',
            'created'
        )

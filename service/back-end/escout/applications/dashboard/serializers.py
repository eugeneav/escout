from rest_framework import serializers
from escout.applications.dashboard.models import Application


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    key = serializers.CharField(required=False, max_length=100)
    name = serializers.CharField(required=False, max_length=100)

    class Meta:
        model = Application
        fields = ('key', 'name')

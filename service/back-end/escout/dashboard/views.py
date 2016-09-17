import logging

from django.db import DatabaseError
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from escout.dashboard.models import Application
from escout.dashboard.serializers import ApplicationSerializer, EventSerializer

from escout.dashboard.models import Event

logger = logging.getLogger(__name__)

"""

    View usage would make code cleaner. See http://www.django-rest-framework.org/tutorial/3-class-based-views/

    TODO:
    1. Setup debug of backend app [done]
    2. Use PostgresSQL on backend [done]
    4. Implement Application CRUD according to django-rest-framework guides [done] Note: Tests required
    5. Implement Events CRUD according to django-rest-framework guides [done]
    6. Finish data collector [done] (use async Python features - Celery)
    6. Find out how to test django app
    7. Refactor application according to Python and Django best practises
    8. Use Fabric for deploy

    Feature in future:
    1. Email actions tracking?
    2. Marketing tool?
    3. Smart logged data analysis?
    4. Behavior research?

    [NOTE]: Start from that file

"""


class ApplicationViewSet(viewsets.ViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def list(self, request):
        auth_token = request.auth.key

        # NOTE Record not found exception might be required,
        # but if token is not exit - application will return invalid token response

        try:
            token_model = Token.objects.get(key=auth_token)
        except Token.DoesNotExist:
            return Response([], 401)  # Rarely possible unauthorized request

        user_model = token_model.user
        account_model = user_model.account
        queryset = account_model.application_set.all()

        serializer = ApplicationSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request):

        auth_token = request.auth.key

        try:
            token_model = Token.objects.get(key=auth_token)
        except Token.DoesNotExist:
            return Response([], 401)  # Rarely possible unauthorized request

        output = {}
        input_data = request.data

        application_serializer = ApplicationSerializer(data=input_data)

        if not application_serializer.is_valid():
            output['status'] = 'invalid_input_data'
            output['data'] = {
                'errors': application_serializer.errors
            }
            return Response(output, 400)

        validated_data = application_serializer.validated_data
        validated_data['account'] = request.user.account

        try:
            output = application_serializer.create(validated_data)
            return Response(output)
        except DatabaseError as error:
            logger.error(error)
            output['status'] = 'application_create_error'
            return Response(output, 500)

    def retrieve(self, request, pk=None):

        auth_token = request.auth.key

        try:
            token_model = Token.objects.get(key=auth_token)
        except Token.DoesNotExist:
            return Response([], 401)

        user_model = token_model.user
        account_model = user_model.account

        output = {}

        try:
            application = account_model.application_set.get(id=pk)
            output['personal_id'] = application.personal_id
            output['title'] = application.title
            output['description'] = application.description
            output['created'] = application.created
            output['modified'] = application.modified
            return Response(output)

        except Application.DoesNotExist:
            output['status'] = 'application_does_not_exists'
            return Response(output, 400)

    def update(self, request, pk=None):

        auth_token = request.auth.key

        try:
            token_model = Token.objects.get(key=auth_token)
        except Token.DoesNotExist:
            return Response([], 401)  # Rarely possible unauthorized request

        output = {}
        input_data = request.data

        application_serializer = ApplicationSerializer(data=input_data)

        if not application_serializer.is_valid():
            output['status'] = 'invalid_input_data'
            output['data'] = {
                'errors': application_serializer.errors
            }
            return Response(output, 400)

        validated_data = application_serializer.validated_data

        try:
            application_model = Application.objects.get(id=pk)
            output = application_serializer.update(application_model, validated_data)
            return Response(output)
        except Application.DoesNotExist:
            output['status'] = 'application_create_error'
            output['data'] = {
                'errors': ''
            }
        except DatabaseError as error:
            logger.error(error)
            output['status'] = 'application_update_error'
            return Response(output, 500)

    def partial_update(self, request, pk=None):
        return Response(status=501)

    def destroy(self, request, pk=None):
        auth_token = request.auth.key

        try:
            token_model = Token.objects.get(key=auth_token)
        except Token.DoesNotExist:
            return Response([], 401)

        user_model = token_model.user
        account_model = user_model.account

        output = {}

        try:
            account_model.application_set.get(id=pk).delete()
            output['status'] = 'application_deleted'
            return Response(output)

        except Application.DoesNotExist:
            output['status'] = 'application_does_not_exists'
            return Response(output, 400)
        pass


class EventViewSet(viewsets.ViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def list(self, request):
        auth_token = request.auth.key

        # NOTE Record not found exception might be required,
        # but if token is not exit - application will return invalid token response

        try:
            token_model = Token.objects.get(key=auth_token)
        except Token.DoesNotExist:
            return Response([], 401)  # Rarely possible unauthorized request

        application_id = request.GET.get('aid', False)
        if not application_id:
            return Response(status=400)

        user_model = token_model.user
        account_model = user_model.account

        output = {}

        try:
            application_model = account_model.application_set.get(id=application_id)
        except Application.DoesNotExist:
            output['status'] = 'application_does_not_exists'
            return Response(output, 400)

        queryset = application_model.event_set.all()

        serializer = EventSerializer(queryset, many=True)

        return Response(serializer.data)

from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from escout.dashboard.models import Application
from escout.dashboard.serializers import ApplicationSerializer

"""

    View usage would make code cleaner. See http://www.django-rest-framework.org/tutorial/3-class-based-views/

    TODO:
    1. Setup debug of backend app [done]
    2. Use PostgresSQL on backend [done]
    4. Implement Application CRUD according to django-rest-framework guides
    5. Implement Events CRUD according to django-rest-framework guides
    6. Finish data collector (use async Python features)
    6. Find out how to test django app
    7. Refactor application according to Python and Django best practises

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

        #data = JSONParser().parse(request)
        application_serializer = ApplicationSerializer(data=input_data)

        if not application_serializer.is_valid():
            output['status'] = 'invalid_input_data'
            output['data'] = {
                'errors': application_serializer.errors
            }
            return JsonResponse(output)

        validated_data = application_serializer.validated_data

        try:
            validated_data['account'] = request.user.account
            application_info = application_serializer.create(validated_data)

            output['status'] = 'ok'
            output['data'] = application_info
            return Response(output)
        except ValidationError:
            output['status'] = 'application_create_error'
            output['data'] = {
                'errors': ''
            }

        return Response(output, 400)

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_applications(request):
    token = request.auth.key

    token_model = Token.objects.get(key=token)
    user_model = token_model.user
    account_model = user_model.account
    applications = account_model.application_set.all()

    apps = []

    for app in applications:
        apps.append(app.title)

        response = JsonResponse({
            'status': 'OK',
            'data': {
                'applications': apps,
                'offset': 0,
                'limit': 0
            }
        })

        response['x-ku-ku'] = "code 1"  # TODO Custom header example

    return response


def put_appliaction(request):
    pass


def post_application(request):
    pass


def update_application(request):
    pass


def delete_application(request):
    pass


def get_app_events(request):
    pass

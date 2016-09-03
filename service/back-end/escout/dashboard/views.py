from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
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


    def list(self, request):

        auth_token = request.auth.key

        token_model = Token.objects.get(key=auth_token)
        user_model = token_model.user
        account_model = user_model.account
        queryset = account_model.application_set.all()

        serializer = ApplicationSerializer(queryset, many=True)

        return Response(serializer.data)



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

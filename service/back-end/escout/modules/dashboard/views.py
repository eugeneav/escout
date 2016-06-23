from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from escout.modules.dashboard.models import Application


# TODO View usage would make code cleaner. See http://www.django-rest-framework.org/tutorial/3-class-based-views/

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

        response['x-ku-ku'] = "code 1" # TODO Custom header example

    return response


def post_application(request):
    pass


def update_application(request):
    pass


def delete_application(request):
    pass

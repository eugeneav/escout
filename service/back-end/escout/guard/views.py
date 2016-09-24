import logging

from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from rest_framework.serializers import ValidationError
from escout.guard.serializers import UserSerializer

logger = logging.getLogger(__name__)


def sign_in(request):
    if request.method == 'POST':
        output = {}
        data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=data)

        if not user_serializer.is_valid():
            output['status'] = 'invalid_input_data'
            output['data'] = {
                'errors': user_serializer.errors
            }
            return JsonResponse(output)

        validated_data = user_serializer.validated_data

        try:
            user = user_serializer.authenticate(validated_data)
            # NOTICE Do not remove created parameter, that makes token.key not available
            token, created = Token.objects.get_or_create(user=user)

            output['status'] = 'ok'
            output['data'] = {
                'token': token.key
            }
        except ValidationError as e:
            logging.exception(e)
            output['status'] = 'invalid_input_data'
            output['data'] = {
                'errors': validated_data
            }

        return JsonResponse(output)


def sign_up(request):
    if request.method == 'POST':
        output = {}
        data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=data)

        if user_serializer.is_valid():
            validated_data = user_serializer.validated_data
            result = user_serializer.create(validated_data)
            output['status'] = result['status']
        else:
            output['status'] = 'invalid_input_data'

        return JsonResponse(output)


def logout(request):
    auth_token = request.META['HTTP_AUTHORIZATION']
    token_parts = auth_token.split(" ")
    token = token_parts[1]

    try:
        token_record = Token.objects.get(key=token)
        token_record.delete()
    except Token.DoesNotExist as e:
        logger.exception(e)

    return JsonResponse({
        'status': 'logged_out',
        'data': {}
    })


# TODO Get password recovery token
def get_password_recovery_token(request):
    return JsonResponse({}, status=501)


# TODO Recover password
def recover_password(request):
    return JsonResponse({}, status=501)

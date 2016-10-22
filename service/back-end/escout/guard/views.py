import time
import json
import logging
import hashlib

from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from rest_framework.serializers import ValidationError
from escout.guard.serializers import UserSerializer

from escout.guard.models import PasswordRecoverToken

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


def get_password_recovery_token(request):
    hostname = request.META['HTTP_HOST']

    response = {
        'status': 'recover_email_sent'
    }

    request_body_json = json.loads(request.body.decode('utf-8'))

    if 'email' in request_body_json:
        email = request_body_json.get('email', None)
        try:
            validate_email(email)

            User.objects.get(email=email)

            recover_token = PasswordRecoverToken()
            recover_token.email = email
            recover_token.token = hashlib.sha256((email + str(time.time())).encode('utf-8')).hexdigest()
            recover_token.save()

            send_mail(
                'Password recovery on %s' % hostname,
                "Dear user,\n To recover your password, please follow a link http://%s/reset/%s \nYours Escout" % (
                    hostname, recover_token.token
                ),
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )

            response['status'] = 'email_sent'

        except ValidationError as e:
            logger.exception(e)
            response['status'] = 'invalid_email'
            return JsonResponse(response, status=400)
        except User.DoesNotExist as e:
            logger.exception(e)
            response['status'] = 'unknown_user'
            return JsonResponse(response, status=400)
        except Exception as e:
            logger.exception(e)
            return JsonResponse(status=500)

    return JsonResponse(response)


# TODO Recover password
def recover_password(request):
    # TODO Change user password

    token = request.POST.get('token', None)
    new_password = request.POST.get('new_pass', None)
    new_password_repeat = request.POST.get('new_pass_rep', None)

    if token and new_password and new_password == new_password_repeat:
        # TODO Find User id by token
        # TODO Change password
        pass

    return JsonResponse({}, status=501)


def check_token(request):
    # TODO Check a token if it is valid
    return JsonResponse({}, status=501)


# TODO Recover password
def change_password(request):
    # TODO Change user password

    return JsonResponse({}, status=501)

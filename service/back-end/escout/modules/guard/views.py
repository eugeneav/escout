from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from escout.modules.guard.serializers import UserSerializer
from rest_framework.serializers import ValidationError


# http://tastypieapi.org/ Another one famous rest framework

# TODO May need to be refactored
def sign_in(request):
    if request.method == 'POST':
        output = {}
        data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=data)
        if user_serializer.is_valid():
            validated_data = user_serializer.validated_data

            try:
                user = user_serializer.authenticate(validated_data)  # TODO
                token, created = Token.objects.get_or_create(user=user)

                output['status'] = 'ok'
                output['data'] = {
                    'token': token.key,
                    'created': created
                }

            except ValidationError:
                output['status'] = 'error'
                output['data'] = {
                    'error': 'User is not active or not exists'  # TODO
                }

        else:
            output['status'] = 'invalid_input_data'
            output['status'] = user_serializer.errors

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

    token_record = Token.objects.get(key=token)
    token_record.delete()

    return JsonResponse({
        'status': 'logged_out',
        'data': {

        }
    })

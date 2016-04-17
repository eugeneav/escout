from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from modules.guard.serializers import UserSerializer


def sign_in(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=data)

        if user_serializer.is_valid():

            user_serializer.validated_data
            user_serializer.create()

        # print(data)

        return JsonResponse(data)


# TODO
def logout(request):
    auth_token = request.META['HTTP_AUTHORIZATION']
    token_parts = auth_token.split(" ")
    token = token_parts[1]

    token_record = Token.objects.get(key=token)
    token_record.delete()

    return JsonResponse({
        'status': 'OK',
        'data': {

        }
    })

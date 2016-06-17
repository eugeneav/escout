from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from escout.modules.dashboard.models import Application
from escout.modules.dashboard.serializers import ApplicationSerializer


# Create your views here.

class ApplicationsViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (IsAuthenticated,)


# @login_required
def get_applications(request):
    applicationRecords = Application.objects.all()

    applications = []

    return JsonResponse({
        'status': 'OK',
        'data': {
            'applications': applications,
            'offset': 0,
            'limit': 0
        }
    })

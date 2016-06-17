from django.conf.urls import url, include
from rest_framework import routers
from escout.modules.dashboard import views

router = routers.DefaultRouter()
router.register(r'applications', views.ApplicationsViewSet, base_name="applications")

urlpatterns = [
    url(r'^', include(router.urls)),
]

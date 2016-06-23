from django.conf.urls import url, include
from rest_framework import routers
from escout.modules.dashboard import views


urlpatterns = [
    url(r'^',  views.get_applications, name="Get applications"),
]

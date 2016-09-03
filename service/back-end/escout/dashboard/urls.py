from django.conf.urls import url

from escout.dashboard import views

urlpatterns = [
    url(r'^', views.get_applications, name="Get applications"),
]

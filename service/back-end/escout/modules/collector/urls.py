from django.conf.urls import url

from . import views

urlpatterns = [
    # Example url(r'^$', views.index, name='index'),
    url(r'^(?P<file_name>.{1,})$', views.track, name='track'),
]

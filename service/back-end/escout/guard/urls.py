from django.conf.urls import url
from rest_framework import routers
from rest_framework.authtoken import views as authtoken_views

from escout.guard import views

router = routers.DefaultRouter()
# router.register(r'applications', views.ApplicationsViewSet, base_name="applications")

urlpatterns = [
    url(r'sign-in', views.sign_in, name='Sign In'),
    url(r'^sign-up', views.sign_up, name='Sign Up'),
    url(r'^login', authtoken_views.obtain_auth_token, name='Login'),
    url(r'^logout', views.logout, name='Logout'),
    # url(r'^', include(router.urls), name=''),
]

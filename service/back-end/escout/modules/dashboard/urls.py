from django.conf.urls import url, include
from rest_framework import routers
from escout.modules.dashboard import views
from rest_framework.authtoken import views as authtoken_views

router = routers.DefaultRouter()
router.register(r'applications', views.ApplicationsViewSet, base_name="applications")

urlpatterns = [
    url(r'^login/', authtoken_views.obtain_auth_token),
    url(r'^logout/', views.logout),
    url(r'^', include(router.urls)),
]

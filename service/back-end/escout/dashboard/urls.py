
from escout.dashboard.views import ApplicationViewSet, EventViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'applications', ApplicationViewSet)
router.register(r'events', EventViewSet)
urlpatterns = router.urls


from escout.dashboard.views import ApplicationViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'applications', ApplicationViewSet)
urlpatterns = router.urls

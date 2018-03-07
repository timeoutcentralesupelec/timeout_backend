from rest_framework import routers
from events.viewsets import EventViewSet

router = routers.DefaultRouter()
router.register(r'events', EventViewSet)
urlpatterns = router.urls

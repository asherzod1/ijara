from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from announcement.views import TransportViewSet, AnnouncementViewSet
from images.views import ImageViewSet
from test.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("transport", TransportViewSet)
router.register("announcement", AnnouncementViewSet)
router.register("images", ImageViewSet)


app_name = "api"
urlpatterns = router.urls

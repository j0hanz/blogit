from rest_framework.routers import DefaultRouter

from .views import FollowerViewSet

router = DefaultRouter()
router.register(r'', FollowerViewSet, basename='follower')

urlpatterns = router.urls

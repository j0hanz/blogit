from rest_framework.routers import DefaultRouter

from likes.views import LikeViewSet

router = DefaultRouter()
router.register(r'', LikeViewSet, basename='like')

urlpatterns = router.urls

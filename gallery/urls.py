from rest_framework.routers import DefaultRouter

from .views import AlbumViewSet, ImageViewSet

router = DefaultRouter()
router.register(r'albums', AlbumViewSet)
router.register(r'images', ImageViewSet)

urlpatterns = router.urls

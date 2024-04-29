from rest_framework import routers

from app.api import AppViewSet

router = routers.SimpleRouter()
router.register(r'exercise', AppViewSet, basename='/exercise')

urlpatterns = router.urls



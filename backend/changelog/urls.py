from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()

router.register("changelog", viewsets.ChangeLogViewSet)

urlpatterns = router.urls

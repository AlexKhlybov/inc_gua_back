from rest_framework.routers import DefaultRouter
from . import viewsets


router = DefaultRouter()

router.register('black_list_item', viewsets.BlackListItemViewSet)

urlpatterns = router.urls

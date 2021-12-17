from rest_framework.routers import DefaultRouter
from . import viewsets


router = DefaultRouter()

router.register('limit_bank', viewsets.LimitBankViewSet)
router.register('limit_principal', viewsets.LimitPrincipalViewSet)
router.register('limit_fz', viewsets.LimitFZViewSet)
router.register('limit', viewsets.LimitViewSet)
router.register('fz_limits', viewsets.FZLimitsViewSet)

urlpatterns = router.urls

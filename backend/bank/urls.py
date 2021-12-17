from rest_framework.routers import DefaultRouter
from . import viewsets


router = DefaultRouter()

router.register('bank', viewsets.BankViewSet)
router.register('bank_document', viewsets.BankDocumentViewSet)
router.register('bank_limits', viewsets.BankLimitsViewSet)
router.register('bank_contract', viewsets.BankСontractViewSet)
router.register('section', viewsets.SectionViewSet)
router.register('document', viewsets.DocumentViewSet)

urlpatterns = router.urls

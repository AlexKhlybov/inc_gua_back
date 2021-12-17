from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()

router.register('beneficiary', viewsets.BeneficiaryViewSet)
router.register('principal', viewsets.PrincipalViewSet)
router.register('principal_financial_indicators', viewsets.PrincipalFinancialIndicatorsViewSet)
router.register('legal_entity', viewsets.LegalEntityViewSet)
router.register('person', viewsets.PersonViewSet)
router.register('co_owner', viewsets.CoOwnerViewSet)
router.register('ownership', viewsets.OwnershipViewSet)

urlpatterns = router.urls

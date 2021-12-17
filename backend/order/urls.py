from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()

router.register('order', viewsets.OrderViewSet)
router.register('order_document', viewsets.OrderDocumentViewSet)
router.register('document_type', viewsets.DocumentTypeViewSet)
router.register('order_special_condition', viewsets.OrderSpecialConditionViewSet)
router.register('contract', viewsets.ContractViewSet)
router.register('lot', viewsets.LotViewSet)
router.register('contest_type', viewsets.ContestTypeViewSet)
router.register('contest', viewsets.ContestViewSet)
router.register('auction', viewsets.AuctionViewSet)
router.register('purchase', viewsets.PurchaseViewSet)
router.register('factors', viewsets.FactorsViewSet)
router.register('quote', viewsets.QuoteViewSet)
router.register('order_factors', viewsets.OrderFactorsViewSet)
router.register('comment', viewsets.CommentViewSet)
router.register('oliver_wyman', viewsets.OliverWymanViewSet)
router.register('accounting_forms', viewsets.AccountingFormViewSet)
router.register('state_log', viewsets.StateLogViewSet)
router.register('order_quote', viewsets.OrderQuoteViewSet)

urlpatterns = router.urls

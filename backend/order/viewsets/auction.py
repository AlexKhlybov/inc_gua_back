from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from app.service import custom_exception_handler
from ..models import Auction
from ..serializers import AuctionSerializer


class AuctionViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer

    def list(self, request, *args, **kwargs):
        return super(AuctionViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(AuctionViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler

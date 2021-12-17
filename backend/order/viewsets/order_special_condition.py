from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from app.service import custom_exception_handler
from ..models import OrderSpecialCondition
from ..serializers import OrderSpecialConditionSerializer


class OrderSpecialConditionViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = OrderSpecialCondition.objects.all()
    serializer_class = OrderSpecialConditionSerializer

    def list(self, request, *args, **kwargs):
        return super(OrderSpecialConditionViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(OrderSpecialConditionViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler

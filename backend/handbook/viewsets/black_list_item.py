from rest_framework.viewsets import ModelViewSet
from app.service import custom_exception_handler
from ..models import BlackListItem
from ..serializers import BlackListItemSerializer


class BlackListItemViewSet(ModelViewSet):
    queryset = BlackListItem.objects.all()
    serializer_class = BlackListItemSerializer

    def list(self, request, *args, **kwargs):
        return super(BlackListItemViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(BlackListItemViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler

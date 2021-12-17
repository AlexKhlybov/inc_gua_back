from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from app.service import custom_exception_handler
from ..models import Document
from ..serializers import DocumentSerializer


class DocumentViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def list(self, request, *args, **kwargs):
        return super(DocumentViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(DocumentViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler

from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from app.service import custom_exception_handler
from ..models import Section
from ..serializers import SectionSerializer


class SectionViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    def list(self, request, *args, **kwargs):
        return super(SectionViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(SectionViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler

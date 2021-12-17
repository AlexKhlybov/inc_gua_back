from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from app.service import custom_exception_handler
from ..models import Person
from ..serializers import PersonPassportDataSerializer


class PersonViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonPassportDataSerializer

    def list(self, request, *args, **kwargs):
        return super(PersonViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PersonViewSet, self).retrieve(request, *args, **kwargs)

    def get_exception_handler(self):
        return custom_exception_handler

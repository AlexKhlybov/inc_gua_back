from rest_framework import serializers

from ..models import LegalEntity
from .person import PersonSerializer, PersonPassportDataSerializer


class LegalEntitySerializer(serializers.ModelSerializer):
    fl = PersonPassportDataSerializer(read_only=True)
    eio = PersonPassportDataSerializer(read_only=True)
    lpr = PersonPassportDataSerializer(read_only=True)
    auditor = PersonSerializer(read_only=True)

    class Meta:
        model = LegalEntity
        fields = [
            'id', 'title', 'other_title', 'type', 'taxation', 'inn', 'kpp', 'registration_date',
            'registration_address', 'actual_address', 'region', 'okved', 'opf', 'average_number_of_employees',
            'regulation_document', 'attorney_document', 'bank_number', 'bank_name', 'bank_inn', 'bank_bik', 'bank_kpp',
            'bank_correspondent_account_cb', 'fl', 'eio', 'eio_date', 'lpr', 'lpr_post', 'auditor',
            'auditor_opinion', 'no_audit', 'create_at', 'update_at'
        ]

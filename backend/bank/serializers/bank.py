from rest_framework import serializers

from ..models import Bank


class BankSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    def get_logo(self, obj):
        return obj.get_logo_url

    class Meta:
        model = Bank
        fields = ['id', 'title', 'inn', 'registration_address', 'bik', 'kpp', 'correspondent_account_cb',
                  'registration_date', 'region', 'license_number', 'eio_surname', 'eio_name', 'eio_patronymic',
                  'eio_appointment_date', 'contact_person_surname', 'contact_person_name', 'contact_patronymic',
                  'email', 'phone', 'logo', 'create_at', 'update_at']

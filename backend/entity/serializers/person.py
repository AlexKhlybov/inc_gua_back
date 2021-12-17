from rest_framework import serializers

from ..models import Person


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ['id', 'last_name', 'first_name', 'patronymic', 'create_at', 'update_at', ]


class PersonPassportDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ['id', 'last_name', 'first_name', 'patronymic', 'birth_date', 'birth_place',
                  'passport_series', 'passport_number', 'department_code',
                  'collect_date', 'collect_by_whom', 'registration_address', 'citizenship', 'create_at', 'update_at']

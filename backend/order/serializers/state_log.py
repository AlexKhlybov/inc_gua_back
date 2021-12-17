from rest_framework import serializers
import logging
from django_fsm_log.models import StateLog

from user.serializers.user import UserSerializer

logger = logging.getLogger(__name__)


class StateLogSerializer(serializers.ModelSerializer):
    by = UserSerializer()

    class Meta:
        model = StateLog
        fields = ('__all__')

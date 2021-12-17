from app.mixins import Timestamps
from ..mixins.alarm import AlarmMixin


class WarningSignal(AlarmMixin, Timestamps):
    pass

    class Meta:
        verbose_name = 'Предупредительный сигнал'
        verbose_name_plural = 'Предупредительные сигналы'

    def __str__(self):
        return self.description

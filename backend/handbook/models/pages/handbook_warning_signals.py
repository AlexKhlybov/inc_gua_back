from garpix_page.models import BasePage
from ...models.warning_signal import WarningSignal


class HandbookWarningSignalsPage(BasePage):

    # template = 'warning_signals.html'

    class Meta:
        verbose_name = 'Страница "Справочник (предупреждающие сигналы)"'
        verbose_name_plural = 'Страницы "Справочники (предупреждающие сигналы)"'

    def get_context(self, request=None, *args, **kwargs):
        from ...serializers import WarningSignalSerializer
        context = super(HandbookWarningSignalsPage, self).get_context(request, *args, **kwargs)
        context.update({
            'items': WarningSignalSerializer(WarningSignal.objects.all(), many=True).data
        })
        return context

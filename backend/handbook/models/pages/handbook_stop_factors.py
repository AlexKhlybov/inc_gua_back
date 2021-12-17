from garpix_page.models import BasePage
from ...models.stop_factor import StopFactor


class HandbookStopFactorsPage(BasePage):
    # template = 'stop_factors.html'

    class Meta:
        verbose_name = 'Страница "Справочник (стоп-факторы)"'
        verbose_name_plural = 'Страницы "Справочники (стоп-факторы)"'

    def get_context(self, request=None, *args, **kwargs):
        from ...serializers import StopFactorSerializer
        context = super(HandbookStopFactorsPage, self).get_context(request, *args, **kwargs)
        context.update({
            'items': StopFactorSerializer(StopFactor.objects.all(), many=True).data
        })
        return context

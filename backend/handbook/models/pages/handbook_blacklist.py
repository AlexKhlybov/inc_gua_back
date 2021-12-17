from garpix_page.models import BasePage
from ..black_list_item import BlackListItem


class HandbookBlacklistPage(BasePage):

    # template = 'black_list.html'

    class Meta:
        verbose_name = 'Страница "Справочник (черный список)"'
        verbose_name_plural = 'Страницы "Справочники (черный список)"'

    def get_context(self, request=None, *args, **kwargs):
        from ...serializers import BlackListItemSerializer
        context = super(HandbookBlacklistPage, self).get_context(request, *args, **kwargs)
        context.update({
            'items': BlackListItemSerializer(BlackListItem.objects.all(), many=True).data
        })
        return context

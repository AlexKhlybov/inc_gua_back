from django.apps import AppConfig


class OrderConfig(AppConfig):
    name = 'order'
    verbose_name = 'Заявка'

    def ready(self):  # noqa
        import order.signals  # noqa

import logging

from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ChangeLog(models.Model):
    class ACTIONS:
        ACTION_CREATE = "create"
        ACTION_UPDATE = "update"
        ACTION_DELETE = "delete"
        TYPES = (
            (ACTION_CREATE, "Заявка создана"),
            (ACTION_UPDATE, "Заявка обновлена"),
            (ACTION_DELETE, "Заявка удалена"),
        )

    changed = models.DateTimeField(auto_now=True, verbose_name="Дата/время изменения")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="Автор изменения", on_delete=models.CASCADE, null=True
    )
    role = models.CharField(max_length=128, verbose_name="Роль пользователя", blank=True)
    action_on_model = models.CharField(choices=ACTIONS.TYPES, max_length=50, verbose_name="Действие", null=True)
    field = models.CharField(max_length=256, verbose_name="Поле", blank=True, default='')
    oldvalue = models.TextField(verbose_name="Предыдущее значение", blank=True, default='')
    newvalue = models.TextField(verbose_name="Текущее значение", blank=True, default='')
    name = models.CharField(max_length=256, verbose_name="Наименование", blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(db_index=True, blank=True, null=True)

    class Meta:
        ordering = ("changed",)
        verbose_name = "Журнал изменений"
        verbose_name_plural = "Журналы изменений"

    def __str__(self):
        return f"{self.id}"

    @staticmethod
    def add(user, action_on_model, inn=None, change_data=None, _id=None, content_type=None):
        """Создание записи в журнале регистрации изменений"""
        name = str(inn) + f'-{_id}'
        try:
            role = user.role
        except Exception as e:
            logging.error(e)
            role = "underwriter"
        if not change_data:
            log = ChangeLog.objects.create(
                user=user,
                role=role,
                content_type=content_type,
                object_id=_id,
                action_on_model=action_on_model,
                name=name)
            return log.pk
        if _id and change_data:
            for k, v in change_data.items():
                log = ChangeLog.objects.create(
                    user=user,
                    role=role,
                    content_type=content_type,
                    object_id=_id,
                    action_on_model=action_on_model,
                    field=k,
                    oldvalue=v[0] if v[0] else '',
                    newvalue=v[1],
                    name=name)
        return log.pk

    @staticmethod
    def get_verbose_field_name(instance, field_name):
        return instance._meta.get_field(field_name).verbose_name.title()

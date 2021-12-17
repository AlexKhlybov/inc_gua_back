from changelog.middleware import LoggedInUser
from changelog.models import ChangeLog as changelog
from django.contrib.contenttypes.models import ContentType


def journal_save_handler(sender, instance, created, **kwargs):
    loggedIn = LoggedInUser()
    filds = instance.diff
    inn = instance.principal.legal_entity.inn
    content_type = ContentType.objects.get_for_model(instance.__class__)
    _id = instance.id
    if created:
        changelog.add(loggedIn.current_user, changelog.ACTIONS.ACTION_CREATE, inn, _id=_id, content_type=content_type)
    else:
        change_data = dict()
        for k, v in filds.items():
            change_data[changelog.get_verbose_field_name(instance, k)] = v
        changelog.add(loggedIn.current_user, changelog.ACTIONS.ACTION_UPDATE, inn, change_data, _id=_id, content_type=content_type)


def journal_delete_handler(sender, instance, **kwargs):
    loggedIn = LoggedInUser()
    inn = instance.principal.legal_entity.inn
    content_type = ContentType.objects.get_for_model(instance.__class__)
    _id = instance.id
    changelog.add(loggedIn.current_user, changelog.ACTIONS.ACTION_DELETE, inn, None, _id, content_type=content_type)

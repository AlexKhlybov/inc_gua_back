from rest_framework.exceptions import ErrorDetail
from rest_framework.views import exception_handler
from django.utils.translation import gettext as _


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    try:
        if response.status_code:
            if response.status_code == 401:
                response.data['detail'] = ErrorDetail(string=_('401.'),
                                                      code='invalid')
            if response.status_code == 403:
                response.data['detail'] = ErrorDetail(string=_('403.'),
                                                      code='permission_denied')
            if response.status_code == 404:
                response.data['detail'] = ErrorDetail(string=_('404.'),
                                                      code='not_found')
            if response.status_code == 405:
                response.data['detail'] = ErrorDetail(string=_('405.'),
                                                      code='method_not_allowed')
        return response
    except Exception:
        return response

import requests
from django.contrib.sites.models import Site
from django.db.models.signals import post_save
from django.dispatch import receiver

from entity.models import Beneficiary
from .models import Order


@receiver(post_save, sender=Order)  # noqa
def request_integration(sender, created, instance, *args, **kwargs):  # noqa
    if created:
        try:
            send_requests(instance)
        except:  # noqa
            print('some connection issues because of difference between tests Site.domain and self host domain')


def send_requests(instance):
    base_url = Site.objects.first().domain
    base_url += 'api/v1/' if base_url.endswith('/') else '/api/v1/'
    principal_financial_indicators = {
        'url': base_url + 'entity/principal_financial_indicators/',
        'json': {
            "title": "string",
            "legal_entity": instance.principal.legal_entity.id
        }
    }
    requests.post(
        url=principal_financial_indicators['url'],
        json=principal_financial_indicators['json']
    )

    limit_principal_calculate = {
        'url': base_url + 'limit/limit_principal/limit_principal_calculate/',
        'json': {
            "inn": instance.principal.legal_entity.inn,
        },
    }
    requests.post(
        url=limit_principal_calculate['url'],
        json=limit_principal_calculate['json']
    )

    update_principal_limits = {
        'url': base_url + 'limit/limit_principal/update_principal_limits/',
        'json': {
            "principal": instance.principal.pk,
        },
    }
    requests.post(
        url=update_principal_limits['url'],
        json=update_principal_limits['json']
    )
    get_factors = {
        'url': base_url + 'order/order/get_factors/',
        'json': {
            "order": instance.pk,
            "description": "string"
        },
    }
    requests.post(
        url=get_factors['url'],
        json=get_factors['json']
    )
    customer = Beneficiary.objects.filter(legal_entity__principal_legal_entity__principal_orders=instance).first()
    # purchase_number = Contract.objects.filter(beneficiary=customer).last()
    olywer_wymans = {
        'url': base_url + 'order/order/olyver_wyman_score_guarantee/',
        'json': {
            "supplierInn": instance.principal.legal_entity.inn,
            # "customerInn": instance.principal.legal_entity.inn,
            "customerInn": customer.inn if customer else instance.principal.legal_entity.inn,
            # "purchaseNumber": f"{purchase_number.pk}" if purchase_number else ''
        },
    }
    requests.post(
        url=olywer_wymans['url'],
        json=olywer_wymans['json']
    )

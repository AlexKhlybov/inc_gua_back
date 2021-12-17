import requests
from django.contrib.sites.models import Site
from app.celery import app
from entity.models import Beneficiary
from ..models import Order


@app.task()
def update_order():
    from config.models import SiteConfiguration
    config = SiteConfiguration.objects.first()
    if config:
        orders = Order.objects.filter(status_state__in=['Blank', 'Something'],
                                      status_retries_count__lt=config.limit_to_retry)
    else:
        orders = Order.objects.filter(status_state__in=['Blank', 'Something'])

    for instance in orders:
        instance.status_retries_count += 1
        is_succesful = update_order_info(instance)
        if is_succesful:
            instance.status_state = 'Done'
        else:
            instance.status_state = 'Something'
        instance.save()


def update_order_info(instance):
    base_url = Site.objects.first().domain + '/api/v1/'
    principal_financial_indicators = {
        'url': base_url + 'entity/principal_financial_indicators/',
        'json': {
            "title": "string",
            "legal_entity": instance.principal.legal_entity.id
        }
    }
    principal_financial_indicators_request = requests.post(url=principal_financial_indicators['url'],
                                                           json=principal_financial_indicators['json'])

    limit_principal_calculate = {
        'url': base_url + 'limit/limit_principal/limit_principal_calculate/',
        'json': {
            "inn": instance.principal.legal_entity.inn,
        },
    }
    limit_principal_calculate_request = requests.post(url=limit_principal_calculate['url'],
                                                      json=limit_principal_calculate['json'])
    update_principal_limits = {
        'url': base_url + 'limit/limit_principal/update_principal_limits/',
        'json': {
            "principal": instance.principal.pk,
        },
    }
    update_principal_limits_request = requests.post(url=update_principal_limits['url'],
                                                    json=update_principal_limits['json'])
    get_factors = {
        'url': base_url + 'order/order/get_factors/',
        'json': {
            "order": instance.pk,
            "description": "string"
        },
    }
    get_factors_request = requests.post(url=get_factors['url'],
                                        json=get_factors['json'])
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
    olywer_wymans_request = requests.post(url=olywer_wymans['url'],
                                          json=olywer_wymans['json'])

    return response_is_valid(principal_financial_indicators_request,
                             limit_principal_calculate_request,
                             update_principal_limits_request,
                             get_factors_request,
                             olywer_wymans_request)


def response_is_valid(*args):
    for item in args:
        if item.status_code not in [200, 201]:
            return False
    return True

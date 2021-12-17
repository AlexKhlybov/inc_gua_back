from rest_framework.test import APITestCase

from order.tests.test_base import BaseTest


class OrderApiTest(APITestCase, BaseTest):
    def setUp(self):
        BaseTest.__init__(self)

    def test_positive_get_order_contract(self):
        url = '/api/v1/order/contract/'
        response = self.client.get(f'{url}')
        self.assertEqual(response.status_code, 200, )

    def test_positive_get_order_orders(self):
        url = '/api/v1/order/order/'
        response = self.client.get(f'{url}')
        self.assertEqual(response.status_code, 200, )

    def test_positive_get_order_order_document_type(self):
        url = '/api/v1/order/document_type/'
        response = self.client.get(f'{url}')
        self.assertEqual(response.status_code, 200, )

    def test_positive_get_order_order_document(self):
        url = '/api/v1/order/order_document/'
        response = self.client.get(f'{url}')
        self.assertEqual(response.status_code, 200, )

    # def test_positive_create_order_document(self):
    #     url = '/api/v1/order/order_document/'
    #     order_document_id = self.create_order_document.id
    #     data_resp = {
    #         "order": self.create_order.id,
    #         "document_title": 'test_doc',
    #         "document_type": order_document_id,
    #         "is_valid": False
    #     }
    #     print(data_resp)
    #     response = self.client.post(f'{url}', data=data_resp)
    #     self.assertEqual(response.status_code, 201, )

    def test_negative_create_order_document(self):
        url = '/api/v1/order/order_document/'
        data_resp = {
            "order": self.create_order.id,
            "document_title": 'test_doc',
            "document_type": 'test',
            "is_valid": False
        }
        print(data_resp)
        response = self.client.post(f'{url}', data=data_resp)
        self.assertEqual(response.status_code, 400, )

    def test_positive_update_order_document(self):
        order_document_id = self.create_order_document.id
        url = f'/api/v1/order/order_document/{order_document_id}/'
        data_resp = {
            'is_valid': True
        }
        response = self.client.put(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )

    def test_positive_get_order_order_special_condition(self):
        url = '/api/v1/order/order_special_condition/'
        response = self.client.get(f'{url}')
        self.assertEqual(response.status_code, 200, )

    # def test_positive_create_order(self):
    #     url = '/api/v1/order/order/'
    #     guaranty = self.create_garanty(1000000, 1000000)
    #     pnt = 'pnt'
    #     eis_link = 'https://cool.ru'
    #     data_resp = {
    #         "status": self.order_status.id,
    #         "principal": self.principal.id,
    #         "beneficiary": self.beneficiary.id,
    #         "guaranty": guaranty.id,
    #         "contest": self.contest.id,
    #         "pnt": pnt,
    #         "eis_link": eis_link,
    #         "start_date": '2021-08-17'
    #     }
    #     response = self.client.post(url, data=data_resp)
    #     self.assertEqual(response.status_code, 201, )

    # def test_negative_create_order(self):
    #     url = '/api/v1/order/order/'
    #     guaranty = self.create_garanty(1000000, 1000000)
    #     pnt = 'pnt'
    #     eis_link = 'https://cool.ru'
    #     data_resp = {
    #         "status": self.order_status.id,
    #         "principal": self.principal.id,
    #         "beneficiary": self.beneficiary.id,
    #         "guaranty": guaranty.id,
    #         "contest": self.contest.id,
    #         "pnt": pnt,
    #         "eis_link": eis_link,
    #         "start_date": '2021-08-17'
    #     }
    #     response = self.client_principal.post(url, data=data_resp)
    #     self.assertEqual(response.status_code, 403, )

    # def test_positive_update_order(self):
    #     order_id = self.create_order.id
    #     url = f'/api/v1/order/order/{order_id}/'
    #     partial_data = {'pnt': 10, 'eis_link': 'https://cool_2.ru'}
    #     response = self.client.put(url, data=partial_data)
    #     self.assertEqual(response.status_code, 200, )
    #
    # def test_negative_update_order(self):
    #     order_id = self.create_order.id
    #     url = f'/api/v1/order/order/{order_id}/'
    #     partial_data = {'pnt': 10, 'eis_link': 'https://cool_2.ru'}
    #     response = self.client_principal.put(url, data=partial_data)
    #     self.assertEqual(response.status_code, 403, )

    def test_notexist_update_order(self):
        order_id = self.bad_id
        url = f'/api/v1/order/order/{order_id}/'
        partial_data = {'pnt': 10, 'eis_link': 'https://cool_2.ru'}
        response = self.client.put(url, data=partial_data)
        self.assertEqual(response.status_code, 404, )

    def test_positive_update_partial_order(self):
        order_id = self.create_order.id
        url = f'/api/v1/order/order/{order_id}/'
        partial_data = {'pnt': 10, 'eis_link': 'https://cool_2.ru'}
        response = self.client.patch(url, data=partial_data)
        self.assertEqual(response.status_code, 200, )
    #
    # def test_negative_update_partial_order(self):
    #     order_id = self.create_order.id
    #     url = f'/api/v1/order/order/{order_id}/'
    #     partial_data = {'pnt': 10, 'eis_link': 'https://cool_2.ru'}
    #     response = self.client_principal.patch(url, data=partial_data)
    #     self.assertEqual(response.status_code, 403, )

    def test_notexist_update_partial_order(self):
        order_id = self.bad_id
        url = f'/api/v1/order/order/{order_id}/'
        partial_data = {'pnt': 10, 'eis_link': 'https://cool_2.ru'}
        response = self.client.patch(url, data=partial_data)
        self.assertEqual(response.status_code, 404, )

    def test_negative_delete_partial_order(self):
        order_id = self.create_order.id
        url = f'/api/v1/order/order/{order_id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 405, )

    def test_notexist_delete_partial_order(self):
        order_id = self.bad_id
        url = f'/api/v1/order/order/{order_id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 405, )

    def test_positive_to_state_underwriting_a_new_application(self):
        order_id = self.create_order.id
        url = '/api/v1/order/order/to_state_underwriting_a_new_application/'
        data_resp = {
            "order": order_id,
            "description": 'test'
        }
        response = self.client_suw.post(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )

    def test_positive_to_state_underwriting_in_progress(self):
        order_id = self.create_order.id
        url = '/api/v1/order/order/to_state_underwriting_in_progress/'
        data_resp = {
            "order": order_id,
            "description": 'test'
        }
        response = self.client_uw.post(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )

    def test_positive_to_state_underwriting_requery(self):
        order_id = self.create_order.id
        url = '/api/v1/order/order/to_state_underwriting_requery/'
        data_resp = {
            "order": order_id,
            "description": 'test'
        }
        response = self.client_uw.post(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )

    def test_positive_to_state_quote_auto(self):
        order_id = self.create_order.id
        url = '/api/v1/order/order/to_state_quote_auto/'
        data_resp = {
            "order": order_id,
            "description": 'test'
        }
        response = self.client_uw.post(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )

    def test_positive_to_state_quote_auction(self):
        order_id = self.create_order.id
        url = '/api/v1/order/order/to_state_quote_auction/'
        data_resp = {
            "order": order_id,
            "description": 'test'
        }
        response = self.client_uw.post(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )

    def test_positive_to_state_quote_individual(self):
        order_id = self.create_order.id
        url = '/api/v1/order/order/to_state_quote_individual/'
        data_resp = {
            "order": order_id,
            "description": 'test'
        }
        response = self.client_uw.post(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )

    def test_positive_to_state_underwriting_refusal(self):
        order_id = self.create_order.id
        url = '/api/v1/order/order/to_state_underwriting_refusal/'
        data_resp = {
            "order": order_id,
            "description": 'test'
        }
        response = self.client_uw.post(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )

    def test_positive_to_state_quote_sent(self):
        order_id = self.create_order.id
        url = '/api/v1/order/order/to_state_quote_sent/'
        data_resp = {
            "order": order_id,
            "description": 'test'
        }
        response = self.client_uw.post(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )

    def test_positive_to_state_in_archive(self):
        order_id = self.create_order.id
        url = '/api/v1/order/order/to_state_in_archive/'
        data_resp = {
            "order": order_id,
            "description": 'test'
        }
        response = self.client_uw.post(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )

    def test_positive_to_state_quote_redefined(self):
        order_id = self.create_order.id
        url = '/api/v1/order/order/to_state_quote_redefined/'
        data_resp = {
            "order": order_id,
            "description": 'test'
        }
        response = self.client_uw.post(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )

    def test_positive_to_state_quote_refusal(self):
        order_id = self.create_order.id
        url = '/api/v1/order/order/to_state_quote_refusal/'
        data_resp = {
            "order": order_id,
            "description": 'test'
        }
        response = self.client_uw.post(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )

    def test_positive_to_state_quote_agreed(self):
        order_id = self.create_order.id
        url = '/api/v1/order/order/to_state_quote_agreed/'
        data_resp = {
            "order": order_id,
            "description": 'test'
        }
        response = self.client_uw.post(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )

    def test_positive_to_state_documents_requery(self):
        order_id = self.create_order.id
        url = '/api/v1/order/order/to_state_documents_requery/'
        data_resp = {
            "order": order_id,
            "description": 'test'
        }
        response = self.client_uw.post(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )

    def test_positive_to_state_documents_signature(self):
        order_id = self.create_order.id
        url = '/api/v1/order/order/to_state_documents_signature/'
        data_resp = {
            "order": order_id,
            "description": 'test'
        }
        response = self.client_uw.post(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )

    def test_positive_to_state_documents_refusal(self):
        order_id = self.create_order.id
        url = '/api/v1/order/order/to_state_documents_refusal/'
        data_resp = {
            "order": order_id,
            "description": 'test'
        }
        response = self.client_uw.post(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )

    def test_positive_to_state_guarantee_issue_requested(self):
        order_id = self.create_order.id
        url = '/api/v1/order/order/to_state_guarantee_issue_requested/'
        data_resp = {
            "order": order_id,
            "description": 'test'
        }
        response = self.client_uw.post(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )

    def test_positive_to_state_guarantee_issued_payment_expected(self):
        order_id = self.create_order.id
        url = '/api/v1/order/order/to_state_guarantee_issued_payment_expected/'
        data_resp = {
            "order": order_id,
            "description": 'test'
        }
        response = self.client_uw.post(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )

    def test_positive_to_state_guarantee_disclaimer(self):
        order_id = self.create_order.id
        url = '/api/v1/order/order/to_state_guarantee_disclaimer/'
        data_resp = {
            "order": order_id,
            "description": 'test'
        }
        response = self.client_uw.post(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )

    def test_positive_to_state_guarantee_valid(self):
        order_id = self.create_order.id
        url = '/api/v1/order/order/to_state_guarantee_valid/'
        data_resp = {
            "order": order_id,
            "description": 'test'
        }
        response = self.client_uw.post(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )

    def test_positive_update_state(self):
        order_id = self.create_order.id
        url = '/api/v1/order/order/update_state/'
        data_resp = {
            "order": order_id,
            "description": 'test'
        }
        response = self.client.post(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )

    def test_positive_delete_order_document(self):
        document_id = self.create_order_document.id
        url = f'/api/v1/order/order_document/{document_id}/'
        response = self.client_uw.delete(url)
        self.assertEqual(response.status_code, 204, )

import json
from django.test.utils import override_settings
from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APITransactionTestCase
from django.contrib.auth.models import User
from .models import Account
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class ApplicationTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        url_sign_up = reverse('sign-up')

        data = {'email': 'johndoe2@test.net', 'password': 'johndoepassword2'}
        response = self.client.post(url_sign_up, data, format='json')

        url = reverse('sign-in')
        data = {'email': 'johndoe2@test.net', 'password': 'johndoepassword2'}
        response = self.client.post(url, data, format='json')
        response_data = json.loads(response.content.decode("utf-8"))
        self.token = response_data['data']['token']

    def test_create_application(self):
        data = {'title': "Test application 1", 'description': "Test application for the metter of testing application"}

        response = self.client.post('/dashboard/applications/', data=data, HTTP_AUTHORIZATION="Token " + self.token)
        response_data = json.loads(response.content.decode("utf-8"))

        self.assertTrue('application' in response_data)
        self.assertTrue('personal_id' in response_data['application'])

    def test_get_applications(self):
        data = {'title': "Test application 1", 'description': "Test application for the metter of testing application"}

        response = self.client.post('/dashboard/applications/', data=data, HTTP_AUTHORIZATION="Token " + self.token)
        response_data = json.loads(response.content.decode("utf-8"))

        response = self.client.get('/dashboard/applications/', HTTP_AUTHORIZATION="Token " + self.token)

        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(len(response_data), 1)
        self.assertEqual(response_data[0]['title'], "Test application 1")


    def test_update_application(self):
        data = {'title': "Test application 1", 'description': "Test application for the metter of testing application"}

        response = self.client.post('/dashboard/applications/', data=data, HTTP_AUTHORIZATION="Token " + self.token)
        response_data = json.loads(response.content.decode("utf-8"))

        application_id = response_data['application']['id']

        data = {'title': "Test application 12", 'description': "Test application for the metter of testing application"}
        response = self.client.put('/dashboard/applications/{}/'.format(application_id), data=data,
                                   HTTP_AUTHORIZATION="Token " + self.token)

        response_data = json.loads(response.content.decode("utf-8"))

        self.assertIn('status', response_data)
        self.assertEqual(response_data['status'], 'application_updated')

    def test_delete_application(self):
        data = {'title': "Test application 1", 'description': "Test application for the metter of testing application"}

        response = self.client.post('/dashboard/applications/', data=data, HTTP_AUTHORIZATION="Token " + self.token)
        response_data = json.loads(response.content.decode("utf-8"))

        application_id = response_data['application']['id']

        data = {'title': "Test application 12", 'description': "Test application for the metter of testing application"}
        response = self.client.delete('/dashboard/applications/{}/'.format(application_id), data=data,
                                      HTTP_AUTHORIZATION="Token " + self.token)

        response_data = json.loads(response.content.decode("utf-8"))

        self.assertIn('status', response_data)
        self.assertEqual(response_data['status'], 'application_deleted')

        pass

    def tearDown(self):
        pass


class EventTest(APITransactionTestCase):
    def setUp(self):
        url_sign_up = reverse('sign-up')

        data = {'email': 'johndoe2@test.net', 'password': 'johndoepassword2'}
        response = self.client.post(url_sign_up, data, format='json')

        url = reverse('sign-in')
        data = {'email': 'johndoe2@test.net', 'password': 'johndoepassword2'}
        response = self.client.post(url, data, format='json')
        response_data = json.loads(response.content.decode("utf-8"))
        self.token = response_data['data']['token']

        data = {'title': "Test application 1", 'description': "Test application for the metter of testing application"}

        response = self.client.post('/dashboard/applications/', data=data, HTTP_AUTHORIZATION="Token " + self.token)
        response_data = json.loads(response.content.decode("utf-8"))

        self.application_personal_id = response_data['application']['personal_id']

    # @override_settings(DEBUG=True)
    def test_create_record(self):
        params = {
            'pid': self.application_personal_id,
            'usi': 5938498940,
            'utz': '-180',
            'nm': 'click',
            'p': 2,
            'stt': '1473527002230',
            'spt': '1473527027805',
            'dsc': 'click on a button'
        }

        response = self.client.get('/collector/__tf.gif', params)

        self.assertEqual(200, response.status_code)

    def test_list_records(self):
        params = {
            'pid': self.application_personal_id,
            'usi': 5938498940,
            'utz': '-180',
            'nm': 'click',
            'tp': 'action',
            'p': 2,
            'stt': '1473527002230',
            'spt': '1473527027805',
            'dsc': 'click on a button'
        }

        self.client.get('/collector/__tf.gif', params)

        params = {
            'pid': self.application_personal_id,
            'usi': 6938498940,
            'utz': '-180',
            'nm': 'click',
            'tp': 'action',
            'p': 2,
            'stt': '1473527002230',
            'spt': '1473527027805',
            'dsc': 'click on a button'
        }

        self.client.get('/collector/__tf.gif', params)

        params = {
            'pid': self.application_personal_id,
            'usi': 7938498940,
            'utz': '-180',
            'nm': 'click',
            'tp': 'action',
            'p': 2,
            'stt': '1473527002230',
            'spt': '1473527027805',
            'dsc': 'click on a button'
        }

        self.client.get('/collector/__tf.gif', params)

        response = self.client.get('/dashboard/events/', {'pid': self.application_personal_id, 'page': 1, 'offset': 2},
                                   HTTP_AUTHORIZATION="Token " + self.token)

        response_data = json.loads(response.content.decode("utf-8"))

        self.assertTrue(len(response_data) == 2)

        self.assertEqual(response_data[1]['user_session_id'], 6938498940)
        self.assertEqual(response_data[0]['user_session_id'], 7938498940)

        response = self.client.get('/dashboard/events/', {'pid': self.application_personal_id, 'page': 2, 'offset': 2},
                                   HTTP_AUTHORIZATION="Token " + self.token)

        response_data = json.loads(response.content.decode("utf-8"))

        self.assertTrue(len(response_data) == 1)
        self.assertEqual(response_data[0]['user_session_id'], 5938498940)

import json
from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Account
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


# Create your tests here.

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
        print(response_data)
        self.token = response_data['data']['token']

    def test_create_application(self):
        data = {'title': "Test application 1", 'description': "Test application for the metter of testing application"}

        response = self.client.post('/dashboard/applications/', data=data, HTTP_AUTHORIZATION="Token " + self.token)
        response_data = json.loads(response.content.decode("utf-8"))
        print(response_data)
        self.assertTrue('application' in response_data)
        self.assertTrue('personal_id' in response_data['application'])

    def test_get_applications(self):
        data = {'title': "Test application 1", 'description': "Test application for the metter of testing application"}

        response = self.client.post('/dashboard/applications/', data=data, HTTP_AUTHORIZATION="Token " + self.token)
        response_data = json.loads(response.content.decode("utf-8"))

        response = self.client.get('/dashboard/applications/', HTTP_AUTHORIZATION="Token " + self.token)

        print(response.request)

        print(type(response))
        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(len(response_data), 1)
        self.assertEqual(response_data[0]['title'], "Test application 1")

        pass

    def test_update_application(self):

        data = {'title': "Test application 1", 'description': "Test application for the metter of testing application"}

        response = self.client.post('/dashboard/applications/', data=data, HTTP_AUTHORIZATION="Token " + self.token)
        response_data = json.loads(response.content.decode("utf-8"))

        print(response_data)

        application_id = response_data['application']['id']

        data = {'title': "Test application 12", 'description': "Test application for the metter of testing application"}
        response = self.client.put('/dashboard/applications/{}/'.format(application_id), data=data, HTTP_AUTHORIZATION="Token " + self.token)

        response_data = json.loads(response.content.decode("utf-8"))

        self.assertIn('status',response_data)
        self.assertEqual(response_data['status'], 'application_updated')

        pass

    def test_delete_application(self):

        data = {'title': "Test application 1", 'description': "Test application for the metter of testing application"}

        response = self.client.post('/dashboard/applications/', data=data, HTTP_AUTHORIZATION="Token " + self.token)
        response_data = json.loads(response.content.decode("utf-8"))

        print(response_data)

        application_id = response_data['application']['id']

        data = {'title': "Test application 12", 'description': "Test application for the metter of testing application"}
        response = self.client.delete('/dashboard/applications/{}/'.format(application_id), data=data, HTTP_AUTHORIZATION="Token " + self.token)

        response_data = json.loads(response.content.decode("utf-8"))

        self.assertIn('status',response_data)
        self.assertEqual(response_data['status'], 'application_deleted')

        pass

    def tearDown(self):
        pass

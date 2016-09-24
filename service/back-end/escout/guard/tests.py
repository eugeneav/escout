import json
from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from .models import Account


# Create your tests here.

class AccountModelTests(TestCase):
    user_mode = None
    account_model = None

    def setUp(self):
        self.user_model = User.objects.create_user('johndoe', 'johndoe@test.net', 'johndoepassword')
        self._create_test_accout()
        pass

    def _create_test_accout(self):
        account = Account()
        account.title = 'Test account 1'
        account.description = 'My test account 1'
        account.owner = User.objects.create_user('johndoe2', 'johndoe2@test.net', 'johndoepassword2')
        account.save()

    def test_get_account_exception(self):
        with self.assertRaises(Account.DoesNotExist):
            Account.objects.get(id=1)

    def test_create_account(self):
        account = Account()
        account.title = 'Test account 2'
        account.description = 'My test account 2'
        account.owner = self.user_model
        account.save()

        account_model = Account.objects.get(title='Test account 2')
        self.assertEqual(account_model.description, 'My test account 2')

    def test_update_account(self):
        account_model = Account.objects.get(title='Test account 1')
        account_model.description = 'My new test account 1'
        account_model.save()

        account_model = Account.objects.get(title='Test account 1')
        self.assertEqual(account_model.description, 'My new test account 1')

    def _delete_account(self):
        Account.objects.get(title='Test account 1').delete()

        with self.assertRaises(Account.DoesNotExist):
            Account.objects.get(title='Test account 1')

    def tearDown(self):
        pass


class AuthorizationTests(APITestCase):
    _token = ''

    def setUp(self):
        pass

    def test_sign_in_fail(self):
        url = reverse('sign-in')
        data = {'email': 'johndoe@test.net', 'password': 'johndoepassword'}
        response = self.client.post(url, data, format='json')

        print(json.loads(response.content.decode("utf-8")))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(b'invalid_input_data', response.content)

    def test_sign_up(self):
        url = reverse('sign-up')
        data = {'email': 'johndoe@test.net', 'password': 'johndoepassword'}
        response = self.client.post(url, data, format='json')

        response_data = json.loads(response.content.decode("utf-8"))
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # TODO Change status code to 201?
        self.assertIn(b'user_created', response.content)

    def test_sign_in_success(self):
        url_sign_up = reverse('sign-up')
        data = {'email': 'johndoe@test.net', 'password': 'johndoepassword'}
        self.client.post(url_sign_up, data, format='json')

        url = reverse('sign-in')
        data = {'email': 'johndoe@test.net', 'password': 'johndoepassword'}
        response = self.client.post(url, data, format='json')

        response_data = json.loads(response.content.decode("utf-8"))
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(b'token', response.content)

    def test_logout(self):

        url_sign_up = reverse('sign-up')
        data = {'email': 'johndoe@test.net', 'password': 'johndoepassword'}
        self.client.post(url_sign_up, data, format='json')

        url_sign_in = reverse('sign-in')
        response = self.client.post(url_sign_in, data, format='json')

        response_data = json.loads(response.content.decode("utf-8"))

        url = reverse('logout')
        response = self.client.post(url, {}, format='json', HTTP_AUTHORIZATION="Token " + response_data['data']['token'])

        response_data = json.loads(response.content.decode("utf-8"))
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(b'logged_out', response.content)

    def tearDown(self):
        pass

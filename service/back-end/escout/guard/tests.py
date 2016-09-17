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
    def setUp(self):
        User.objects.create_user('johndoe', 'johndoe@test.net', 'johndoepassword')
        pass

    def test_sign_in(self):
        url = reverse('sign-in')
        data = {'email': 'johndoe@test.net', 'password': 'johndoepassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertIn('token', response.content)

    def test_sign_up(self):
        url = reverse('sign-in')
        data = {'email': 'johndoe@test.net', 'password': 'johndoepassword'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # TODO Change status code to 201?
        # self.assert( 'user_created', response.content)

    def tearDown(self):
        pass

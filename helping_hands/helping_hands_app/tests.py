
import unittest

from django.test import Client, TestCase
from django.contrib.auth.models import User
from helping_hands_app.models import Event, Choice, ITUUser, ITUUserManager, NGOUser


class RegistrationTest(TestCase):  

    def setUp(self):      
        pass

    def tearDown(self):
        pass   

    def test_registration_api_creates_new_user(self):
        c = Client()
        response = c.post('/register/', {'username': 'john123',
                                         'password': 'smith123',
                                         'email': 'smith@asdf.com',
                                         'first_name':'John',
                                         'last_name':'smith',
                                         'security_question':'mother maiden name',
                                         'security_answer':'andrews',
                                         'gender':'male',
                                         'phone_number':'1231231233'
                                          })

        self.assertEqual(response.status_code, 302)
        saved_user = ITUUser.objects.filter(username='smith@asdf.com')

        self.assertEqual(len(saved_user), 1)

    def test_registration_api_fails_if_user_exists(self):
        c = Client()
        response = c.post('/register/', {'username': 'john123',
                                         'password': 'smith123',
                                         'email': 'smith@asdf.com',
                                         'first_name':'John',
                                         'last_name':'smith',
                                         'security_question':'mother maiden name',
                                         'security_answer':'andrews',
                                         'gender':'male',
                                         'phone_number':'1231231233'})
        second_response = c.post('/register/', {'username': 'john123',
                                         'password': 'smith123',
                                         'email': 'smith@asdf.com',
                                         'first_name':'John',
                                         'last_name':'smith',
                                         'security_question':'mother maiden name',
                                         'security_answer':'andrews',
                                         'gender':'male',
                                         'phone_number':'1231231233'})

        
        self.assertEqual(second_response.status_code, 400)
        saved_user = ITUUser.objects.filter(username='smith@asdf.com')
        # still should only have one
        self.assertEqual(len(saved_user), 1)


    def test_login_api_good(self):
        c = Client()        

        ituUser = ITUUser.objects.create_user('email',
                                            'testusername',
                                            'first_name',
                                            'last_name',
                                            'security_question',
                                            'security_answer',
                                            'gender',
                                            '1234564566',
                                             password='pass')
        ituUser.save()

        import pdb; pdb.set_trace()
        response = c.post('/login/', {'username': 'testusername',
                                        'email': 'email',
                                        'password': 'pass'})
        self.assertEqual(response.status_code, 200)


    def test_login_api_bad(self):
        c = Client()

        response = c.post('/login/', {'username': 'testusername',
                                        'email': 'email',
                                        'password': 'badpassword'})
        self.assertEqual(response.status_code, 400)


    def test_logout_api_good(self):
        c = Client()        

        ituUser = ITUUser.objects.create_user('email1',
                                             'username1',
                                             'first_name',
                                             'last_name',
                                             'security_question',
                                             'security_answer',
                                             'gender',
                                             '4564567899',
                                             password='password')

        response = c.post('/login/', {'username': 'username1',
                                        'email': 'email1',
                                        'password': 'password'})
        logout_response = c.post('/logout/', {'username': 'username1'})
        self.assertEqual(logout_response.status_code, 200)


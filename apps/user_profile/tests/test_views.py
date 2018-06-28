# -*- coding=utf-8 -*-
import json
from django.test import TestCase
from apps.user_profile.models import Profile, Request
from apps.user_profile.forms import ProfileForm


class IndexViewTests(TestCase):

    def test_index_view_uses_appropriate_template(self):
        """Index view uses index.html"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_returns_model_data(self):
        """Index view returns model data"""
        response = self.client.get('/')
        data = Profile.objects.first()
        self.assertEqual(response.context['data'], data)

    def test_renders_model_data(self):
        """IndexView renders model data in template"""
        data = Profile.objects.first()
        response = self.client.get('/')
        self.assertIn(data.first_name, response.content)
        self.assertIn(data.last_name, response.content)
        self.assertIn(str(data.date_birth), response.content)
        self.assertIn(data.email, response.content)
        self.assertIn(data.jabber, response.content)
        self.assertIn(data.skype, response.content)
        self.assertIn(data.other_contacts, response.content)
        self.assertIn(data.bio, response.content)
        self.assertIn(str(data.photo), response.content)

    def test_returns_first_if_two_records(self):
        """IndexView returns first record if two records in db"""
        Profile.objects.create(first_name='Test')
        response = self.client.get('/')
        data = Profile.objects.first()
        self.assertEqual(response.context['data'], data)

    def test_renders_cyrillic(self):
        """IndexView renders cyrillic in template"""
        data = Profile.objects.first()
        data.first_name = 'Тест'
        data.save()
        response = self.client.get('/')
        self.assertIn(data.first_name, response.content)

    def test_renders_login_link_if_user_not_logged(self):
        """Renders login link if user not logged"""
        response = self.client.get('/')
        self.assertIn('<a href="/login/">Login</a>', response.content)

    def test_renders_edit_link_if_user_logged(self):
        """Renders edit link if user logged"""
        self.client.login(username='admin', password='admin')
        response = self.client.get('/')
        self.assertIn('<a href="/edit/">Edit</a>', response.content)

    def test_renders_logout_link_if_user_logged(self):
        """Renders logout link if user logged"""
        self.client.login(username='admin', password='admin')
        response = self.client.get('/')
        self.assertIn('<a href="/logout/">Logout</a>', response.content)


class RequestsViewTests(TestCase):

    def test_uses_appropriate_template(self):
        """RequestsView uses requests.html"""
        response = self.client.get('/requests/')
        self.assertTemplateUsed(response, 'requests.html')

    def test_returns_ten_requests(self):
        """RequestsView returns last ten requests"""
        for number in range(20):
            url = '/test/' + str(number)
            self.client.get(url)
        response = self.client.get(
            '/requests/',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        requests = json.loads(response.content)
        saved_requests = list(Request.objects.order_by('-added')[:10])
        self.assertEqual(requests[0]['fields']['http_inf'],
                         saved_requests[0].http_inf)
        self.assertEqual(requests[9]['fields']['http_inf'],
                         saved_requests[9].http_inf)


class EditViewTests(TestCase):

    def test_uses_appropriate_template(self):
        """EditView uses edit.html"""
        response = self.client.get('/edit/')
        self.assertTemplateUsed(response, 'edit.html')

    def test_returns_form(self):
        """EditView returns ProfileForm"""
        response = self.client.get('/edit/')
        self.assertIsInstance(response.context['form'], ProfileForm)

    def test_renders_form(self):
        """EditView renders form with data"""
        form = ProfileForm(instance=Profile.objects.first())
        response = self.client.get('/edit/')
        self.assertIn(form['first_name'].label_tag(), response.content)
        self.assertIn(str(form['first_name']), response.content)
        self.assertIn(form['last_name'].label_tag(), response.content)
        self.assertIn(str(form['last_name']), response.content)
        self.assertIn(form['date_birth'].label_tag(), response.content)
        self.assertIn(str(form['date_birth']), response.content)
        self.assertIn(form['email'].label_tag(), response.content)
        self.assertIn(str(form['email']), response.content)
        self.assertIn(form['jabber'].label_tag(), response.content)
        self.assertIn(str(form['jabber']), response.content)
        self.assertIn(form['skype'].label_tag(), response.content)
        self.assertIn(str(form['skype']), response.content)
        self.assertIn(form['other_contacts'].label_tag(), response.content)
        self.assertIn(str(form['other_contacts']), response.content)
        self.assertIn(form['bio'].label_tag(), response.content)
        self.assertIn(str(form['bio']), response.content)
        self.assertIn(form['photo'].label_tag(), response.content)
        self.assertIn(str(form['photo']), response.content)

    def test_saves_Post(self):
        """EditView saves data if get POST request"""
        self.client.post('/edit/', data={
            u'bio': [u'Test'], u'first_name': [u'Test'],
            u'last_name': [u'Test'], u'date_birth': [u'2000-01-01'],
            u'other_contacts': [u'+380630000000'], u'skype': [u'testskype'],
            u'email': [u'test@testmail.com'], u'jabber': [u'test@jabber.com'],
            u'csrfmiddlewaretoken': [u'XGI9e500JzRRAifdgPxHKR59YJFFId8B'],
        })
        bio = Profile.objects.first()
        self.assertEqual(bio.first_name, 'Test')
        self.assertEqual(bio.last_name, 'Test')
        self.assertEqual(str(bio.date_birth), '2000-01-01')
        self.assertEqual(bio.other_contacts, '+380630000000')
        self.assertEqual(bio.email, 'test@testmail.com')
        self.assertEqual(bio.skype, 'testskype')
        self.assertEqual(bio.jabber, 'test@jabber.com')
        self.assertEqual(bio.bio, 'Test')

    def test_returns_success(self):
        """EditView returns success message if data valid"""
        response = self.client.post('/edit/', data={
            u'bio': [u'Test'], u'first_name': [u'Test'],
            u'last_name': [u'Test'], u'date_birth': [u'2000-01-01'],
            u'other_contacts': [u'+380630000000'], u'skype': [u'testskype'],
            u'email': [u'test@testmail.com'], u'jabber': [u'test@jabber.com'],
            u'csrfmiddlewaretoken': [u'XGI9e500JzRRAifdgPxHKR59YJFFId8B'],
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        success_msg = {'msg': 'Changes have been saved'}
        self.assertEqual(
            json.loads(response.content),
            success_msg
        )

    def test_returns_error(self):
        """EditView returns error message if data invalid"""
        response = self.client.post('/edit/', data={
            u'bio': [u''], u'first_name': [u''],
            u'last_name': [u''], u'date_birth': [u'01-01-2000'],
            u'other_contacts': [u'+380630000000'],
            u'email': [u'test@testmail'], u'skype': [u''],
            u'csrfmiddlewaretoken': [u'XGI9e500JzRRAifdgPxHKR59YJFFId8B'],
            u'jabber': [u'testjabber.com'],
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        errors = {
            "bio": ["This field is required."],
            "first_name": ["This field is required."],
            "last_name": ["This field is required."],
            "date_birth": ["Enter a valid date."],
            "skype": ["This field is required."],
            "jabber": ["Enter a valid email address."],
            "email": ["Enter a valid email address."]
        }
        self.assertEqual(
            json.loads(response.content),
            errors
        )


class AuthSysTests(TestCase):

    def test_login_view_uses_appropriate_template(self):
        """Login view uses login.html"""
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'login.html')

    def test_logout_view_redirect_to_index(self):
        """Logout view redirects to index page"""
        response = self.client.get('/logout/')
        self.assertRedirects(response, '/')

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

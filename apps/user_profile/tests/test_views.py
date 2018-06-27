from django.test import TestCase
from apps.user_profile.models import Profile


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

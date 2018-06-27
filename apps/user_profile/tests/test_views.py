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

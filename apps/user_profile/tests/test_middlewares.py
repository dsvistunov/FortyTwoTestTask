from django.test import TestCase
from apps.user_profile.models import Request


class TestMiddleware(TestCase):

    def test_saves_last_request(self):
        """Tests request middleware saves last request"""
        test_request = 'http://testserver/test'
        self.client.get(test_request)
        saved_request = Request.objects.last()
        self.assertEqual(test_request, str(saved_request))

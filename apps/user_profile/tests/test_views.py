from django.test import TestCase


class IndexViewTests(TestCase):

    def test_index_view_uses_appropriate_template(self):
        """Index view uses index.html"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_index_view_returns_hardcoded_data(self):
        """Index view returns hardcoded data"""
        data = {
            "first_name": "Denis",
            "last_name": "Svistunov",
            "date_birth": "1991-04-19",
            "bio": "Lorem ipsum dolor sit amet.",
            "email": "d.svistunov1991@gmail.com",
            "jabber": "d.svistunov@42cc.co",
            "skype": "d.svistunov",
            "other_contacts": "+380632028013"
        }
        response = self.client.get('/')
        self.assertEqual(response.context['data'], data)

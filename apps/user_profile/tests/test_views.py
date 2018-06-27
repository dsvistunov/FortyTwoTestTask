from django.test import TestCase


class IndexViewTests(TestCase):

    def test_index_view_uses_appropriate_template(self):
        """Index view uses index.html"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

from django.test import TestCase


class EditLinkTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')
        self.edit_link = '<a href="/admin/user_profile/profile/1/">(admin)</a>'

    def test_not_renders_if_not_logged(self):
        """Not renders if user not logged"""
        self.assertNotIn(self.edit_link, self.response.content)

    def test_renders_if_login(self):
        """Tag renders if user logged"""
        self.client.login(username='admin', password='admin')
        response = self.client.get('/')
        self.assertIn(self.edit_link, response.content)

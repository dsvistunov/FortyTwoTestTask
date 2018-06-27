from django.test import TestCase
from apps.user_profile.models import Profile


class ProfileModelTests(TestCase):

    def test_stores_data_from_fixtures(self):
        """Profile model stores data loaded from fixtures"""
        profile = Profile.objects.first()
        self.assertEqual(profile.first_name, 'Denis')
        self.assertEqual(profile.last_name, 'Svistunov')
        self.assertEqual(str(profile.date_birth), '1991-04-19')
        self.assertEqual(profile.email, 'd.svistunov1991@gmail.com')
        self.assertEqual(profile.jabber, 'd.svistunov@42cc.co')
        self.assertEqual(profile.skype, 'd.svistunov')
        self.assertEqual(profile.other_contacts, '+380632028013')
        self.assertEqual(profile.bio, 'Lorem ipsum dolor sit amet.')

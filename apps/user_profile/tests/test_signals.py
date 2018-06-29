from django.test import TestCase
from apps.user_profile.models import Profile, SignalEntry


class SignalsTest(TestCase):

    def setUp(self):
        self.profile = {
            "first_name": "Test",
            "last_name": "Testing",
            "date_birth": "2018-06-21",
            "bio": "Lorem ipsum dolor sit amet.",
            "email": "test@testmail.com",
            "jabber": "test@test.com",
            "skype": "test",
            "other_contacts": "some contacts"
        }

    def test_object_create(self):
        """SignalEntry increments on one if Biography record created"""
        count_before = SignalEntry.objects.count()
        biography = Profile.objects.create(**self.profile)
        count_after = SignalEntry.objects.count()
        self.assertEqual(count_after - 1, count_before)

        signal_entry = SignalEntry.objects.latest('added')
        self.assertIsNotNone(signal_entry)
        self.assertEqual(signal_entry.model, biography._meta.object_name)
        self.assertEquals(signal_entry.instance, unicode(biography))
        self.assertEquals(signal_entry.action, SignalEntry.CREATE)

    def test_object_update(self):
        """SignalEntry increments on one if Biography record updated"""
        count_before = SignalEntry.objects.count()
        biography = Profile.objects.get()
        biography.first_name = 'Testing'
        biography.save()
        count_after = SignalEntry.objects.count()
        self.assertEqual(count_after - 1, count_before)

        signal_entry = SignalEntry.objects.latest('added')
        self.assertIsNotNone(signal_entry)
        self.assertEqual(signal_entry.model, biography._meta.object_name)
        self.assertEquals(signal_entry.instance, unicode(biography))
        self.assertEquals(signal_entry.action, SignalEntry.UPDATE)

    def test_object_delete(self):
        """SignalEntry increments on one if Biography record deleted"""
        count_before = SignalEntry.objects.count()
        biography = Profile.objects.get()
        biography.delete()
        count_after = SignalEntry.objects.count()
        self.assertEqual(count_after - 1, count_before)

        signal_entry = SignalEntry.objects.latest('added')
        self.assertIsNotNone(signal_entry)
        self.assertEqual(signal_entry.model, biography._meta.object_name)
        self.assertEquals(signal_entry.instance, unicode(biography))
        self.assertEquals(signal_entry.action, SignalEntry.DELETE)

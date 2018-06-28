from django.test import TestCase
from apps.user_profile.forms import ProfileForm


class ProfileFormTests(TestCase):

    def test_form_saves_data(self):
        """ProfileForm saves valid data"""
        form = ProfileForm({
            'first_name': 'Test',
            'last_name': 'Testing',
            'date_birth': '2000-01-01',
            'email': 'test@testmail.com',
            'jabber': 'test@jabber.com',
            'skype': 'testskype',
            'other_contacts': '+380630000000',
            'bio': 'Test'
        })
        self.assertTrue(form.is_valid())
        form = form.save()
        self.assertEqual(form.first_name, 'Test')
        self.assertEqual(form.last_name, 'Testing')
        self.assertEqual(str(form.date_birth), '2000-01-01')
        self.assertEqual(form.email, 'test@testmail.com')
        self.assertEqual(form.jabber, 'test@jabber.com')
        self.assertEqual(form.skype, 'testskype')
        self.assertEqual(form.other_contacts, '+380630000000')
        self.assertEqual(form.bio, 'Test')

    def test_blank_data(self):
        """BiographyForm not saves blank data"""
        form = ProfileForm({})
        self.assertFalse(form.is_valid())
        # date_birth not required
        errors = {
            'first_name': [u'This field is required.'],
            'last_name': [u'This field is required.'],
            'email': [u'This field is required.'],
            'jabber': [u'This field is required.'],
            'skype': [u'This field is required.'],
            'other_contacts': [u'This field is required.'],
            'bio': [u'This field is required.']
        }
        self.assertEqual(form.errors, errors)

    def test_form_not_saves_invalid_data(self):
        """BiographyForm not saves invalid data"""
        form = ProfileForm({
            'first_name': 'Test',
            'last_name': 'Testing',
            'date_birth': '01-01-2000',  # wrond data format
            'email': 'testtestmail.com',  # email field must contain @
            'jabber': 'test@jabber.com',
            'skype': 'testskype',
            'other_contacts': '+380630000000',
            'bio': 'Test'
        })
        raised = False
        try:
            form.save()
        except ValueError:
            raised = True
        self.assertTrue(raised)

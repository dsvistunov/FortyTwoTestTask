# -*- coding=utf-8 -*-
import re
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
        self.assertEqual(
            profile.bio,
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
            'Integer imperdiet sit amet nulla in tristique. Nam ullamc'
            'orper velit id venenatis dapibus. Nullam sit amet feugiat'
            ' libero, vitae molestie ligula. Morbi pretium, ante id bl'
            'andit maximus, lectus felis suscipit tellus, a posuere es'
            't odio at ipsum. Orci varius natoque penatibus et magnis '
            'dis parturient montes, nascetur ridiculus mus. Fusce fini'
            'bus sollicitudin eros, id gravida velit lacinia at. Nulla'
            'm pulvinar turpis vel lorem molestie, eget mattis diam da'
            'pibus.'
        )

    def test_entry_is_not_cyrillic(self):
        """Profile model entry isn't contain cyrillic"""
        profile = Profile.objects.first()
        self.assertFalse(bool(re.search('[а-яА-Я]', profile.first_name)))
        self.assertFalse(bool(re.search('[а-яА-Я]', profile.last_name)))
        self.assertFalse(bool(re.search('[а-яА-Я]', profile.email)))
        self.assertFalse(bool(re.search('[а-яА-Я]', profile.jabber)))
        self.assertFalse(bool(re.search('[а-яА-Я]', profile.skype)))
        self.assertFalse(bool(re.search('[а-яА-Я]', profile.other_contacts)))
        self.assertFalse(bool(re.search('[а-яА-Я]', profile.bio)))
        # change to cyrillic
        profile.first_name = 'Тест'
        profile.save()
        self.assertTrue(bool(re.search('[а-яА-Я]', profile.first_name)))

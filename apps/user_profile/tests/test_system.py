import os
from django.test import TestCase
from fortytwo_test_task.settings import BASE_DIR


class SystemTest(TestCase):

    def test_makefile_is_exist(self):
        """Tests that tha makefile is exist in folder"""
        assert os.path.exists(os.path.join(BASE_DIR, 'Makefile')) == 1

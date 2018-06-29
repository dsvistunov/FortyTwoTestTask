from django.test import TestCase
from django.core.management import get_commands, call_command


class ModelListCommandTest(TestCase):

    def test_model_list_call(self):
        """Command not raise error"""
        command = 'model_list'
        commands = get_commands()
        self.assertIn(command, commands)
        error = False
        try:
            call_command(command)
        except:
            error = True
        self.assertFalse(error)

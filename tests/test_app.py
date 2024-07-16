from io import StringIO
from os import getcwd
from sys import path
import unittest.mock
__PR_PATH = getcwd()
path.append(__PR_PATH)

import unittest
from unittest.mock import patch
from web_parser.app import views, parser
from tests.fixtures import message_out


class TestParser(unittest.TestCase):

    def test_user_querry(self):
        '''Check positiv user input'''
        user_input = ['Python', 'Java']
        expected_querry = ['python', 'java']
        with patch('builtins.input', side_effect=user_input):
            querry1 = views.get_user_params()
            querry2 = views.get_user_params()
        self.assertEqual(querry1, expected_querry[0])
        self.assertEqual(querry2, expected_querry[1])


    def test_negative_querry(self):
        '''Check negative user input'''
        user_input = ['','\n']
        with patch('builtins.input', side_effect=user_input):
            querry1 = views.get_user_params()
            querry2 = views.get_user_params()
        self.assertEqual(querry1, '')
        self.assertEqual(querry2, '')


    def test_message_out(self):
        '''Check function message_out'''
        with patch('sys.stdout', new_callable=StringIO) as buffer:
            views.send_message_out()
        fake_out = buffer.getvalue()
        self.assertEqual(fake_out, message_out.expected_message)


    def test_print_result_none(self):
        expected_result ='\nБури на Марсе не позволяют сегодня найти нужную'\
        '\nВам информацию. Попробуйте завтра.\n'
        with patch('sys.stdout', new_callable=StringIO) as buffer:
            views.printed_result(None)
        fake_out = buffer.getvalue()
        self.assertEqual(fake_out, expected_result)


if __name__ == '__main__':
    unittest.main()

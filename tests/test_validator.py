import unittest

from client.cli import parse_args
from client.validator import validate_args


class TestValidateArgs(unittest.TestCase):

    def test_validate_args_no_options(self):
        error, message = validate_args(parse_args([]))
        self.assertTrue(error)
        self.assertTrue('Error: Missing options' in message)

    def test_validate_args_no_command(self):
        error, message = validate_args(parse_args(
            ['--dci-login', 'foo', '--dci-password', 'bar']))
        self.assertTrue(error)
        self.assertTrue('Error: Missing commands' in message)

    def test_validate_args_concat_errors(self):
        _, message = validate_args(parse_args([]))
        self.assertTrue('Error: Missing options' in message)
        self.assertTrue('Error: Missing commands' in message)
        self.assertTrue('Available commands:' in message)

    def test_validate_args_command_not_in_available_commands(self):
        error, message = validate_args(parse_args(
            ['--dci-login', 'foo', '--dci-password', 'bar', 'unknown-command']))
        self.assertTrue(error)
        self.assertTrue('Available commands:' in message)

    def test_validate_args_valid(self):
        error, message = validate_args(parse_args(
            ['--dci-login', 'foo', '--dci-password', 'bar', 'job-list']))
        self.assertFalse(error)
        self.assertEqual(message, "")

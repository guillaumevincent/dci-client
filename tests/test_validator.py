import unittest

from client.cli import parse_args
from client.validator import validate_args


class TestValidateArgs(unittest.TestCase):
    def test_validate_args_no_auth_options(self):
        error, message = validate_args(parse_args([]))
        self.assertTrue(error)
        self.assertTrue("Missing OPTIONS --dci-login and --dci-password" in message)

    def test_validate_args_no_command(self):
        error, message = validate_args(
            parse_args(["--dci-login", "foo", "--dci-password", "bar"])
        )
        self.assertTrue(error)
        self.assertTrue("Error: Invalid COMMAND" in message)

    def test_validate_args_no_resource(self):
        error, message = validate_args(
            parse_args(["--dci-login", "foo", "--dci-password", "bar", "list"])
        )
        self.assertTrue(error)
        print(message)
        self.assertTrue("Error: Invalid RESOURCE" in message)

    def test_validate_args_concat_errors(self):
        _, message = validate_args(parse_args([]))
        self.assertTrue("Error: Missing OPTIONS" in message)
        self.assertTrue("Error: Invalid RESOURCE" in message)
        self.assertTrue("Error: Invalid COMMAND" in message)

    def test_validate_args_command_not_in_available_commands(self):
        error, message = validate_args(
            parse_args(
                ["--dci-login", "foo", "--dci-password", "bar", "unknown-command"]
            )
        )
        self.assertTrue(error)
        self.assertTrue("Available commands:" in message)

    def test_validate_args_command_not_in_available_resources(self):
        error, message = validate_args(
            parse_args(["--dci-login", "foo", "--dci-password", "bar", "list", "job"])
        )
        self.assertTrue(error)
        self.assertTrue("Available resources:" in message)

    def test_validate_args_valid(self):
        error, message = validate_args(
            parse_args(["--dci-login", "foo", "--dci-password", "bar", "list", "jobs"])
        )
        self.assertFalse(error)
        self.assertEqual(message, "")

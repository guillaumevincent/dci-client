import sys
import unittest
import mock
from click.testing import CliRunner

from client.cli import cli, execute


def run_and_exit(cli_args=None):
    """Run dci-client executable"""
    if cli_args is None:
        cli_args = []

    # Fool client so that it believes we're running from CLI instead of pytest
    orig_argv = sys.argv
    sys.argv = ['dcictl'] + cli_args

    try:
        with mock.patch('client.cli.execute') as m:
            m.side_effect = execute
            result = CliRunner().invoke(cli, cli_args)
            context = m.call_args[0][0]
        return result, context
    finally:
        sys.argv = orig_argv


class TestCli(unittest.TestCase):

    def test_call_with_username_and_password(self):
        result, context = run_and_exit(
            ['--dci-login', 'foo', '--dci-password', 'bar'])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(context['dci_login'], 'foo')
        self.assertEqual(context['dci_password'], 'bar')

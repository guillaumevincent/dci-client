import unittest

from mock import patch

from client.cli import parse_args


class TestCli(unittest.TestCase):

    def test_parse_args_dci_cs_url(self):
        args = parse_args(['--dci-cs-url', 'https://api.example.org'])
        self.assertEqual(args.dci_cs_url, 'https://api.example.org')

    def test_parse_args_default_dci_cs_url(self):
        args = parse_args([])
        self.assertEqual(args.dci_cs_url, 'https://api.distributed-ci.io')

    def test_parse_args_DCI_CS_URL_env_variable(self):
        with patch.dict('os.environ', {'DCI_CS_URL': 'https://api.example.org'}):
            args = parse_args([])
            self.assertEqual(args.dci_cs_url, 'https://api.example.org')

    def test_parse_args_dci_login(self):
        args = parse_args(['--dci-login', 'foo'])
        self.assertEqual(args.dci_login, 'foo')

    def test_parse_args_no_dci_login(self):
        args = parse_args([])
        self.assertEqual(args.dci_login, None)

    def test_parse_args_DCI_LOGIN_env_variable(self):
        with patch.dict('os.environ', {'DCI_LOGIN': 'foo'}):
            args = parse_args([])
            self.assertEqual(args.dci_login, 'foo')

    def test_cli_overload_DCI_LOGIN_env_variable(self):
        with patch.dict('os.environ', {'DCI_LOGIN': 'bar'}):
            args = parse_args(['--dci-login', 'foo'])
            self.assertEqual(args.dci_login, 'foo')

    def test_parse_args_dci_password(self):
        args = parse_args(['--dci-password', 'bar'])
        self.assertEqual(args.dci_password, 'bar')

    def test_parse_args_DCI_PASSWORD_env_variable(self):
        with patch.dict('os.environ', {'DCI_PASSWORD': 'bar'}):
            args = parse_args([])
            self.assertEqual(args.dci_password, 'bar')

    def test_cli_overload_DCI_PASSWORD_env_variable(self):
        with patch.dict('os.environ', {'DCI_PASSWORD': 'bar'}):
            args = parse_args(['--dci-password', 'foo'])
            self.assertEqual(args.dci_password, 'foo')

    def test_parse_args_no_dci_password(self):
        args = parse_args([])
        self.assertEqual(args.dci_password, None)

    def test_parse_args_no_verbose(self):
        args = parse_args([])
        self.assertEqual(args.verbose, False)

    def test_parse_args_verbose(self):
        args = parse_args(['--verbose'])
        self.assertEqual(args.verbose, True)

    def test_parse_args_command(self):
        args = parse_args(['list-jobs'])
        self.assertEqual(args.command, 'list-jobs')

    def test_parse_args_default_command(self):
        args = parse_args([])
        self.assertEqual(args.command, 'status')

    def test_parse_args_limit(self):
        args = parse_args(['list-jobs', '--limit', '1'])
        self.assertEqual(args.limit, 1)

    def test_parse_args_default_limit(self):
        args = parse_args([])
        self.assertEqual(args.limit, 10)

    def test_parse_args_sort(self):
        args = parse_args(['list-jobs', '--sort', 'created_at'])
        self.assertEqual(args.sort, 'created_at')

    def test_parse_args_default_sort(self):
        args = parse_args([])
        self.assertEqual(args.sort, None)

    def test_parse_args_where(self):
        args = parse_args(['list-jobs', '--where', 'team_id:abc'])
        self.assertEqual(args.where, [{'key': 'team_id', 'value': 'abc'}])

    def test_parse_args_multiple_where(self):
        args = parse_args(
            ['list-jobs', '--where', 'team_id:abc,remoteci_id:def'])
        self.assertEqual(args.where, [
            {'key': 'team_id', 'value': 'abc'},
            {'key': 'remoteci_id', 'value': 'def'}
        ])

    def test_parse_args_default_where(self):
        args = parse_args([])
        self.assertEqual(args.where, [])

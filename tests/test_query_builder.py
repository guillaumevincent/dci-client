import unittest

from client.cli import parse_args
from client.query_builder import Query


class TestQueryBuilder(unittest.TestCase):
    def test_job_list_command(self):
        args = parse_args(["--dci-login", "foo", "--dci-password", "bar", "job-list"])
        query = Query(args)
        self.assertEqual(query.method, "GET")
        self.assertEqual(query.url, "https://api.distributed-ci.io/api/v1/jobs")
        self.assertDictEqual(query.headers, {})
        self.assertDictEqual(query.data, {})

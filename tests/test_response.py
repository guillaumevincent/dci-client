import unittest

from client.cli import parse_args
from client.response import ResponseHandler


class FakedHttpResponse(object):
    def __init__(self, data, status_code=200):
        self.data = data
        self.status_code = status_code

    def json(self):
        return self.data


class TestResponseHandler(unittest.TestCase):
    def test_response_head_depend_on_resource(self):
        data = [
            {
                "state": "active",
                "name": "jdoe",
                "role_id": "506c6c4e-fc57-475c-a6b4-e1268178b606",
                "fullname": "John Doe",
                "id": "a86caa1b-051d-4c83-bfd6-3f2188842c0d",
                "etag": "17ff4f36-f1e5-4d4a-92c3-fef1dc8d3100",
                "sso_username": "jdoe@example.org",
                "updated_at": "2018-12-10T22:55:56.122926",
                "created_at": "2018-12-10T22:55:56.122926",
                "team_id": "d43a7b29-c15c-492f-9d7c-dc034da4912f",
                "timezone": "UTC",
                "email": "jdoe@example.org",
            },
            {
                "sso_username": "bdylan@example.org",
                "fullname": "Bob Dylan",
                "email": "bdylan@example.org",
                "team_id": "a6f2a6e5-470e-4b52-962f-856683e06680",
                "id": "3f4d509c-6f75-47ba-8e13-f2abd0dac1cd",
                "updated_at": "2018-12-10T22:55:56.122926",
                "name": "bdylan",
                "state": "active",
                "etag": "c2c673b3-ec10-4388-a823-a09792e2220a",
                "timezone": "UTC",
                "created_at": "2018-12-10T22:55:56.122926",
                "role_id": "db02e503-f2e0-4d01-a74c-49ae270b710e",
            },
        ]
        response = ResponseHandler(
            FakedHttpResponse({"users": data}), parse_args(["list", "users"])
        )
        self.assertListEqual(response.data, data)
        self.assertListEqual(
            response.head, ["id", "name", "email", "state", "timezone"]
        )

    def test_response_401(self):
        response = ResponseHandler(
            FakedHttpResponse(
                {
                    "message": "Invalid user credentials",
                    "payload": {},
                    "status_code": 401,
                },
                401,
            ),
            parse_args(["list", "users"]),
        )
        self.assertListEqual(
            response.data, [{"error": "Invalid user credentials", "status code": 401}]
        )
        self.assertListEqual(response.head, ["error", "status code"])

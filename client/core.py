import sys

import requests
from requests.auth import HTTPBasicAuth

from client.cli import parse_args
from client.validator import validate_args
from client.query_builder import Query
from client.printer import Printer
from client.response import ResponseHandler


def main(args=sys.argv[1:]):
    args = parse_args(args)
    error, error_message = validate_args(args)
    if error:
        msg = (
            """Usage: dcictl [OPTIONS] COMMAND RESOURCE [ARGS]
%s
Example:
    # user foo want to list all users
    > dcictl --dci-login foo --dci-password bar list users
"""
            % error_message
        )
        print(msg)
        sys.exit(0)
    auth = HTTPBasicAuth(args.dci_login, args.dci_password)
    query = Query(args)
    response = ResponseHandler(
        requests.request(
            method=query.method,
            url=query.url,
            headers=query.headers,
            data=query.data,
            auth=auth,
        ),
        args,
    )
    if response.data:
        result = Printer(head=response.head).to_string(response.data)
        print(result)

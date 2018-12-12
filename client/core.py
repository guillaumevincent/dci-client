import sys

import requests
from requests.auth import HTTPBasicAuth

from client.cli import parse_args
from client.validator import validate_args
from client.query_builder import Query


def main(args=sys.argv[1:]):
    args = parse_args(args)
    error, error_message = validate_args(args)
    if error:
        print("Usage: dcictl [OPTIONS] COMMAND [ARGS]\n")
        print(error_message)
        print(
            """Example:
    # list all job for user foo and password bar
    > dcictl --dci-login foo --dci-password bar job-list\n"""
        )
        sys.exit(0)
    auth = HTTPBasicAuth(args.dci_login, args.dci_password)
    query = Query(args)
    response = requests.request(
        method=query.method,
        url=query.url,
        headers=query.headers,
        data=query.data,
        auth=auth,
    )
    print(response)
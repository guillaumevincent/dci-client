import sys

from client.cli import parse_args


def main(args=sys.argv[1:]):
    args = parse_args(args)
    print(args)

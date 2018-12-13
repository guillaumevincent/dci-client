import argparse
import os


class WhereAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(WhereAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        where = namespace.where
        for value in values.split(","):
            key, value = value.split("=")
            where.append({"key": key, "value": value})
        setattr(namespace, self.dest, where)


class CommandAction(argparse.Action):
    def __init__(self, *args, **kwargs):
        super(CommandAction, self).__init__(*args, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        if namespace.help:
            values = "help"
        setattr(namespace, self.dest, values.lower())


def parse_args(args):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "--dci-cs-url",
        dest="dci_cs_url",
        help="DCI control server url, default to 'https://api.distributed-ci.io'.",
        default=os.environ.get("DCI_CS_URL", "https://api.distributed-ci.io"),
    )
    parser.add_argument(
        "--dci-login",
        dest="dci_login",
        help="DCI login or 'DCI_LOGIN' environment variable.",
        default=os.environ.get("DCI_LOGIN"),
    )
    parser.add_argument(
        "--dci-password",
        dest="dci_password",
        help="DCI password or 'DCI_PASSWORD' environment variable.",
        default=os.environ.get("DCI_PASSWORD"),
    )
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--sort")
    parser.add_argument("--where", action=WhereAction, default=[], nargs="*")
    parser.add_argument("-h", "--help", action="store_true")
    parser.add_argument("command", action=CommandAction, nargs="?", default="help")
    parser.add_argument("resource", nargs='?')
    return parser.parse_args(args)

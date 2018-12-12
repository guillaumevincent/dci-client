from client.command import available_commands


class AuthRule(object):
    def __init__(self, args):
        self.args = args
        self.error_message = None

    def is_valid(self):
        if not self.args.dci_login or not self.args.dci_password:
            self.error_message = (
                """Error: Missing options --dci-login and --dci-password"""
            )
            return False
        return True


class CommandRule:
    def __init__(self, args):
        self.args = args
        self.error_message = None

    def is_valid(self):
        error_message = """Error: Missing commands

Available commands:
    job-list                        List all jobs.
"""
        if self.args.command is None:
            self.error_message = error_message
            return False
        if self.args.command not in available_commands:
            self.error_message = error_message
            return False
        return True


def validate_args(args):
    rules = [AuthRule(args), CommandRule(args)]
    error = False
    error_message = ""
    for rule in rules:
        if not rule.is_valid():
            error = True
            error_message += "%s\n" % rule.error_message
    return error, error_message

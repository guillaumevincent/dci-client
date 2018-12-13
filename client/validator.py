from client.query_builder import available_commands, available_resources


class AuthRule(object):
    def __init__(self, args):
        self.args = args
        self.error_message = ""

    def is_valid(self):
        if not self.args.dci_login or not self.args.dci_password:
            self.error_message = """Error: Missing OPTIONS --dci-login and --dci-password
       or set DCI_LOGIN and DCI_PASSWORD env variable
"""
            return False
        return True


class ResourceRule(object):
    def __init__(self, args):
        self.args = args
        self.error_message = ""

    def is_valid(self):
        is_valid = True
        if self.args.resource not in available_resources:
            self.error_message += (
                """\nError: Invalid RESOURCE\nAvailable resources: %s"""
                % ", ".join(available_resources)
            )
            is_valid = False
        return is_valid


class CommandRule:
    def __init__(self, args):
        self.args = args
        self.error_message = ""

    def is_valid(self):
        is_valid = True
        if self.args.command not in available_commands:
            self.error_message += (
                """\nError: Invalid COMMAND\nAvailable commands: %s"""
                % ", ".join(available_commands)
            )
            is_valid = False
        return is_valid


def validate_args(args):
    rules = [AuthRule(args), CommandRule(args), ResourceRule(args)]
    error = False
    error_message = ""
    for rule in rules:
        if not rule.is_valid():
            error = True
            error_message += "%s\n" % rule.error_message
    return error, error_message

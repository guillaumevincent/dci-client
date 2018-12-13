available_commands = ["list", "get", "create", "update", "delete"]

available_resources = ["jobs", "users"]

methods_commands = {
    "list": "GET",
    "get": "GET",
    "create": "POST",
    "update": "PUT",
    "delete": "DELETE",
}


class Query(object):
    def __init__(self, args):
        self.method = methods_commands[args.command]
        self.url = "{}/api/v1/{}".format(args.dci_cs_url, args.resource)
        self.headers = {}
        self.data = {}

from client.command import commands_endpoints


class Query(object):
    def __init__(self, args):
        self.method = "GET"
        self.url = "{}{}".format(args.dci_cs_url, commands_endpoints[args.command])
        self.headers = {}
        self.data = {}

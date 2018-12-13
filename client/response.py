heads_resources = {"users": ["id", "name", "email", "state", "timezone"]}


class ResponseHandler(object):
    def __init__(self, http_response, args):
        self.status_code = http_response.status_code
        if self.status_code == 200:
            resource = args.resource
            self.data = http_response.json()[resource]
            self.head = heads_resources[resource]

        if self.status_code == 401:
            self.data = [
                {
                    "error": http_response.json()["message"],
                    "status code": self.status_code,
                }
            ]
            self.head = ["error", "status code"]

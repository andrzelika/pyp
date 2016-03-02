import json

def parse_json(func):
    def parse(self, request, *args, **kwargs):
        request.data = json.loads(request.read())
        return func(self, request, *args, **kwargs)
    return parse

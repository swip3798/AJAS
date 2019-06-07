import json

class Serializer():
    def serialize(self, object):
        return json.dumps(object)

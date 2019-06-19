import bottle
from bottle import request, route, Bottle
from .serializer import Serializer

class Api():

    def __init__(self):
        self.resolvers_get = {}
        self.resolvers_post = {}
        self.serializer = Serializer()
        self.app = Bottle()
        self.app.route('<path:path>', method="GET", callback=self.get_callback)
        self.app.route('<path:path>', method="POST", callback=self.post_callback)
        self.blocks = []

    
    def add_block(self, block):
        self.blocks.append(block)


    def add_get_resolver(self, path, resolver):
        self.resolvers_get[path] = resolver
    
    def add_post_resolver(self, path, resolver):
        self.resolvers_post[path] = resolver

    def get_callback(self, path):
        query = request.query.dict
        for i in query:
            query[i] = query[i][0]
        for i in self.blocks:
            if i.prefix == path[:len(i.prefix)]:
                return self.serializer.serialize(i.resolver_get(path[len(i.prefix):], request.headers, query))
        return self.serializer.serialize(self.resolvers_get[path](request.headers, query))
    
    def post_callback(self, path):
        query = request.forms.dict
        for i in query:
            query[i] = query[i][0]
        for i in self.blocks:
            if i.prefix == path[:len(i.prefix)]:
                return self.serializer.serialize(i.resolver_post(path[len(i.prefix):], request.headers, query))
        return self.serializer.serialize(self.resolvers_post[path](request.headers, query))

    def run(self, host, port, server='wsgiref'):
        self.app.run(host = host, port = port, server = server)
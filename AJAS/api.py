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


    def add_get_resolver(self, path, resolver):
        self.resolvers_get[path] = resolver
    
    def add_post_resolver(self, path, resolver):
        self.resolvers_post[path] = resolver

    def get_callback(self, path):
        return self.serializer.serialize(self.resolvers_get[path](request.headers, request.query))
    
    def post_callback(self, path):
        return self.serializer.serialize(self.resolvers_post[path](request.headers, request.forms))

    def run(self, host, port, server='wsgiref'):
        self.app.run(host = host, port = port, server = server)
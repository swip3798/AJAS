import bottle
from .serializer import Serializer
from flask import Flask, request

class Api():
    '''
    Central object of AJAS, runs the actual webserver. 
    Allows to add resolvers to paths and automatically serializes their return values.
    Allows to add Blocks for purposes like authentication, versioning etc.
    '''
    def __init__(self):
        self.resolvers_get = {}
        self.resolvers_post = {}
        self.serializer = Serializer()
        self.app = Flask(__name__)
        self.app.add_url_rule('/<path:path>', "get", self.get_callback, methods=["GET"])
        self.app.add_url_rule('/<path:path>', "post", self.post_callback, methods=["POST"])
        self.blocks = []

    
    def add_block(self, block):
        self.blocks.append(block)


    def add_get_resolver(self, path, resolver):
        '''
        path: String => URL-path
        resolver: Function => resolver function with the signature res(header, query)
        '''
        self.resolvers_get[path] = resolver
    
    def add_post_resolver(self, path, resolver):
        '''
        path: String => URL-path
        resolver: Function => resolver function with the signature res(header, query)
        '''
        self.resolvers_post[path] = resolver

    def get_callback(self, path):
        '''
        Internal method
        Calls the specific resolver for the paths and serializes the return value
        '''
        query = request.args
        path = "/" + path
        for i in self.blocks:
            if i.prefix == path[:len(i.prefix)]:
                return self.serializer.serialize(i.resolver_get(path[len(i.prefix):], request.headers, query))
        return self.serializer.serialize(self.resolvers_get[path](request.headers, query))
    
    def post_callback(self, path):
        '''
        Internal method
        Calls the specific resolver for the paths and serializes the return value
        '''
        query = request.form
        path = "/" + path
        for i in self.blocks:
            if i.prefix == path[:len(i.prefix)]:
                return self.serializer.serialize(i.resolver_post(path[len(i.prefix):], request.headers, query))
        return self.serializer.serialize(self.resolvers_post[path](request.headers, query))

    def run(self, host, port):
        '''
        Runs the webserver which hosts the Api.
        host: String => IP-Adress which the server listens to, use "0.0.0.0" for all
        port: int => Port on which the server listens
        server: String => Server system which AJAS should use, look up on the bottle framework for the server options https://bottlepy.org/docs/dev/deployment.html#server-options
        '''
        self.app.run(host = host, port = port)
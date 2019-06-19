from .api import Api
from .exceptions import AuthException

class Block(Api):

    def __init__(self, prefix, authenticator = None):
        super().__init__()
        self.prefix = prefix
        self.authenticator = authenticator
        self.app = None
        self.blocks = None
        self.run = None
        self.add_block = None

    def resolver_get(self, path, headers, query):
        if self.authenticator is not None:
            if self.authenticator.authenticate(path, headers, query):
                return self.resolvers_get[path](headers, query)
            else:
                raise AuthException("Path " + path + " requires authentication")
        else:
            return self.resolvers_get[path](headers, query)

    def resolver_post(self, path, headers, query):
        if self.authenticator is not None:
            if self.authenticator.authenticate(path, headers, query):
                return self.resolvers_post[path](headers, query)
            else:
                raise AuthException("Path " + path + " requires authentication")
        else:
            return self.resolvers_post[path](headers, query)
class Block():

    def __init__(self, prefix, authenticator = None):
        self.prefix = prefix
        self.authenticator = None
        self.resolvers_get = {}
        self.resolvers_post = {}
    
    def add_get_resolver(self, path, resolver):
        self.resolvers_get[path] = resolver
    
    def add_post_resolver(self, path, resolver):
        self.resolvers_post[path] = resolver
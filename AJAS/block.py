from AJAS import Api

class Block(Api):

    def __init__(self, prefix, authenticator = None):
        super().__init__()
        self.prefix = prefix
        self.authenticator = authenticator
        self.app = None
        self.blocks = None
        self.run = None
        self.add_block = None
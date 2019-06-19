import unittest
from AJAS import Api, Serializer, Block, Authenticator, AuthException

class Unitests_Api(unittest.TestCase):
    def test_init(self):
        # Test simply the init of the Api Object
        api = Api()
        self.assertEqual(api.resolvers_get, {}, "Resolver for GET is not initial")
        self.assertEqual(api.resolvers_post, {}, "Resolver for POST is not initial")
    
    def test_add_get_resolver(self):
        # Test the functionality of the add_get_resolver of the Api object
        self.api.add_get_resolver("/testpath", lambda x, y: {"test": 1})
        self.assertEqual(len(self.api.resolvers_get), 1, "GET resolver was not added")
        self.assertEqual(list(self.api.resolvers_get.keys()), ["/testpath"], "Path is wrong")
        self.assertEqual(self.api.resolvers_get["/testpath"](1, 1), {"test": 1}, "Callback function does not return expected value")

    def test_add_post_resolver(self):
        # Test the functionality of the add_post_resolver of the Api object
        self.api.add_post_resolver("/testpath", lambda x, y: {"test": 1})
        self.assertEqual(len(self.api.resolvers_post), 1, "POST resolver was not added")
        self.assertEqual(list(self.api.resolvers_post.keys()), ["/testpath"], "Path is wrong")
        self.assertEqual(self.api.resolvers_post["/testpath"](1, 1), {"test": 1}, "Callback function does not return expected value")

    def test_blocks_get(self):
        # Test the functionality of Blocks in get requests
        v1 = Block("/v1")
        v1.add_get_resolver("/testpath", lambda x, y: {"test": 1})
        self.api.add_block(v1)
        self.assertEqual(len(self.api.blocks), 1, "Blocks are not added")
    
    def setUp(self):
        # For every test a new initial Api object is used
        self.api = Api()

    def tearDown(self):
        self.api = None

class SerializerTests(unittest.TestCase):
    def test_serialize(self):
        # Test if the json Serializer works correctly
        s = Serializer()
        self.assertEqual(s.serialize({"test": 1}), '{"test": 1}')

if __name__ == '__main__':
    unittest.main()
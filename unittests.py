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

    def test_callback_get(self):
        # Test the functionality of the callback_get of the Api object
        self.api.add_get_resolver("/testpath", lambda x, y: {"test": 1})
        jsonstr = self.api.get_callback("/testpath")
        self.assertEqual(jsonstr, '{"test": 1}', "JSON string is wrong")

    def test_blocks_get(self):
        # Test the functionality of Blocks in get requests
        v1 = Block("/v1")
        v1.add_get_resolver("/testpath", lambda x, y: {"test": 1})
        self.api.add_block(v1)
        jsonstr = self.api.get_callback("/v1/testpath")
        self.assertEqual(jsonstr, '{"test": 1}', "JSON string is wrong")
    
    def test_auth_positive(self):
        # Test the functionality of the authenticator system with the normal positive authenticator
        auth = Authenticator()
        v1 = Block("/v1", auth)
        v1.add_get_resolver("/testpath", lambda x, y: {"test": 1})
        self.api.add_block(v1)
        jsonstr = self.api.get_callback("/v1/testpath")
        self.assertEqual(jsonstr, '{"test": 1}', "JSON string is wrong")

    def test_auth_negative(self):
        # Test the functionality of the authenticator system with a negative authenticator
        class Negative_Auth(Authenticator):
            def authenticate(self, path, headers, query):
                    return not super().authenticate(path, headers, query)
        auth = Negative_Auth()
        v1 = Block("/v1", auth)
        v1.add_get_resolver("/testpath", lambda x, y: {"test": 1})
        self.api.add_block(v1)
        exception_raised = False
        try:
            jsonstr = self.api.get_callback("/v1/testpath")
        except AuthException:
            exception_raised = True
        self.assertEqual(exception_raised, True, "No exception was raised")
    
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
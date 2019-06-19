import unittest
from AJAS import Api, Serializer, Block

class Unitests_Api(unittest.TestCase):
    def test_init(self):
        api = Api()
        self.assertEqual(api.resolvers_get, {}, "Resolver for GET is not initial")
        self.assertEqual(api.resolvers_post, {}, "Resolver for POST is not initial")
    
    def test_add_get_resolver(self):
        self.api.add_get_resolver("/testpath", lambda x, y: {"test": 1})
        self.assertEqual(len(self.api.resolvers_get), 1, "GET resolver was not added")
        self.assertEqual(list(self.api.resolvers_get.keys()), ["/testpath"], "Path is wrong")
        self.assertEqual(self.api.resolvers_get["/testpath"](1, 1), {"test": 1}, "Callback function does not return expected value")

    def test_add_post_resolver(self):
        self.api.add_post_resolver("/testpath", lambda x, y: {"test": 1})
        self.assertEqual(len(self.api.resolvers_post), 1, "POST resolver was not added")
        self.assertEqual(list(self.api.resolvers_post.keys()), ["/testpath"], "Path is wrong")
        self.assertEqual(self.api.resolvers_post["/testpath"](1, 1), {"test": 1}, "Callback function does not return expected value")

    def test_callback_get(self):
        self.api.add_get_resolver("/testpath", lambda x, y: {"test": 1})
        jsonstr = self.api.get_callback("/testpath")
        self.assertEqual(jsonstr, '{"test": 1}', "JSON string is wrong")

    def test_blocks_get(self):
        v1 = Block("/v1")
        v1.add_get_resolver("/testpath", lambda x, y: {"test": 1})
        self.api.add_block(v1)
        jsonstr = self.api.get_callback("/v1/testpath")
        self.assertEqual(jsonstr, '{"test": 1}', "JSON string is wrong")
    
    def setUp(self):
        self.api = Api()

    def tearDown(self):
        self.api = None

class SerializerTests(unittest.TestCase):
    def test_serialize(self):
        s = Serializer()
        self.assertEqual(s.serialize({"test": 1}), '{"test": 1}')

if __name__ == '__main__':
    unittest.main()
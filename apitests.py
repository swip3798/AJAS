import unittest
import requests
import threading
from AJAS import Api, Block, Authenticator, AuthException
import json
import time

def set_up_server():
    api = Api()
    def echo_query(header, query):
        return query
    def echo_header(header, query):
        return header
    def hello_world(header, query):
        return {"hello":"world"}
    class MyAuth(Authenticator):
        def authenticate(self, path, header, query):
            return header['HTTP_AUTHORIZATION'] == "testauth"
    with_auth = Block("/auth", MyAuth())
    no_auth = Block("/noauth")
    with_auth.add_get_resolver("/echo/query", echo_query)
    with_auth.add_post_resolver("/echo/query", echo_query)
    no_auth.add_get_resolver("/echo/query", echo_query)
    no_auth.add_post_resolver("/echo/query", echo_query)
    api.add_block(with_auth)
    api.add_block(no_auth)
    api.add_get_resolver("/helloworld", hello_world)
    api.run("localhost", 8080)

class RequestTests(unittest.TestCase):
    def test_hello_world(self):
        res = requests.get("http://localhost:8080/helloworld")
        self.assertEqual(json.loads(res.text), {"hello":"world"}, "Hello World is not responding correctly")
    
    def test_query_get_no_auth(self):
        res = requests.get("http://localhost:8080/noauth/echo/query?hello=world")
        self.assertEqual(json.loads(res.text), {"hello":"world"}, "Query get no auth not correctly echoed")

    def test_query_get_auth(self):
        res = requests.get("http://localhost:8080/auth/echo/query?hello=world", headers = {"Authorization": "testauth"})
        self.assertEqual(json.loads(res.text), {"hello":"world"}, "Query get no auth not correctly echoed")

    def test_query_post_no_auth(self):
        res = requests.post("http://localhost:8080/noauth/echo/query", data={"hello":"world"})
        self.assertEqual(json.loads(res.text), {"hello":"world"}, "Query get no auth not correctly echoed")

    def test_query_post_auth(self):
        res = requests.post("http://localhost:8080/auth/echo/query", data={"hello":"world"}, headers = {"Authorization": "testauth"})
        self.assertEqual(json.loads(res.text), {"hello":"world"}, "Query get no auth not correctly echoed")
    

    
if __name__ == "__main__":
    threading._start_new_thread(set_up_server, ())
    time.sleep(1)
    unittest.main()
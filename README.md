# AJAS
[![Build Status](https://travis-ci.org/swip3798/AJAS.svg?branch=master)](https://travis-ci.org/swip3798/AJAS)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Generic badge](https://img.shields.io/badge/Python%20Version-3.x-green.svg)]()
## Description  
Another JSON Api Server. This is a library for Python 3 to create fast JSON-Rest APIs. It uses flask and gevent in the background.
## Usage
A simple start:
```python
from AJAS import Api

def simple_resolver(header, query):
    return {"hello":"world"}

api = Api()
api.add_get_resolver("/hello", simple_resolver)
api.add_post_resolver("/hello", simple_resolver)
api.run("localhost", 8080)
```
This will run an webserver returning `'{"hello":"world"}'` at the adress `http://localhost:8080/hello` for both GET and POST requests.

### Using blocks
Using blocks allows you to seperate different parts of your API. This can be used for versioning. Also, blocks can hold a authenticator, which can accept or deny a request based on the header and query of the reuest.

```python
from AJAS import Api, Authenticator

class MyAuth(Authenticator):
    def authenticate(self, header, query):
        if someCheck() == True:
            return True
        else:
            return False

def simple_resolver(header, query):
    return {"hello":"world"}

api = Api()
v1 = Block("/v1")
v1.add_get_resolver("/hello", resolver)
api.add_block(v1)
api.run("localhost", 8080)
```

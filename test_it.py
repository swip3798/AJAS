from AJAS import Api

def resolver(header, query):
    return {"hi":int(query.get("hello")), "lol": 2}

api = Api()
api.add_get_resolver("/hello", resolver)
api.run("0.0.0.0", 8080, server="tornado")
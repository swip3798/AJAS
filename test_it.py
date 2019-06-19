from AJAS import Api, Block

def resolver(header, query):
    return {"hi":int(query["hello"]), "lol": 2}

api = Api()
v1 = Block("/v1")
v1.add_get_resolver("/hello", resolver)
v1.add_post_resolver("/hello", resolver)
api.add_block(v1)
api.run("0.0.0.0", 8080)
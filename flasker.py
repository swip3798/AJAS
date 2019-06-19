from flask import Flask

def index():
    return "hello"

app = Flask(__name__)
app.add_url_rule("/", "index", index)
app.run("localhost", 8080)
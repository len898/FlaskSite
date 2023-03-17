from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Index</p>"


@app.route("/hello")
def hello_world():
    return "<p>Hello World</p>"

#escape makes sure that text entered cannot be code, and is rendered as text 
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}"

@app.route("/post/<int:post_id>")
def post(post_id):
    return f"The post, {escape(post_id)}"

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        pass
    else:
        pass
    
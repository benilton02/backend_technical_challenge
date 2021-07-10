
from flask import Flask, request

app = Flask("myAPI")

@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!"

@app.route("/signup", methods=["POST"])
def sign_up():
    body = request.get_json()
    print(body)
    return {"id": 0}


def run_api():
    app.run()

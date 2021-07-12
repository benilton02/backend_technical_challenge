from config import app, db
import requests, json
from flask import request
from src.models.order import (add_user,
                              data_user, 
                              show_all)



@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!"


@app.route("/credit", methods=["POST"])
def resquest_credit():
    body = request.json
    admin = add_user(body)
    return ({"ticket" : str(admin.id) }, 201)


@app.route("/credit/<int:post_id>", methods=["GET"])
def get(post_id):
    user = data_user(post_id)
    if user.status is True:
        return "Approved"
    else:
        return "Denied"


@app.route("/all", methods=["GET"])
def get_all():
    return (json.dumps(show_all()), 200)

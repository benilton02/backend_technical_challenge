from typing import NoReturn
from config import app, db
import requests, json
from flask import request
from src.models.order import (add_user,
                              data_user, 
                              show_all)



@app.errorhandler(404)
def not_found(e):
    print(e, flush=True)
    return "Page does not exist", 404


@app.route("/hello", methods=["GET"])
def hello_world():
    print("Hello World! ",  flush=True)
    return "Hello World!"


@app.route("/credit", methods=["POST"])
def resquest_credit():
    body = request.json
    admin = add_user(body)
    ticket = {"ticket" : str(admin.id) }
    return ticket, 201


@app.route("/credit/<int:post_id>", methods=["GET"])
def get(post_id):
    user = data_user(post_id)
    if user is not None:
        if user.status is True:
            status = "Approved!"
        else:
            status = "Denied!"
        return status, 200
    else:
        return "Page does not exist", 404
    

@app.route("/all", methods=["GET"])
def get_all():
    all_users = show_all()
    return (json.dumps(all_users), 200)

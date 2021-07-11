from config import app, db
import requests, json
from flask import request
from src.models.order import Order


@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!"


@app.route("/credit", methods=["POST"])
def resquest_credit():
    body = request.json
    admin = Order( 
                name = body["name"],
                age = body["age"],
                credit = body["credit"] 
            )

    db.session.add(admin)
    db.session.commit()
    return {"id": 0}


@app.route("/credit", methods=["GET"])
def get():
    orders = Order.query.all()
    data = []

    for order in orders:
        data.append({
            "name": order.name,
            "age": order.age,
            "credit": order.credit
        })
    return (json.dumps(data), 200)
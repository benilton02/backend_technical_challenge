from config import app, db
import requests, json
from flask import request
from src.models.order import Order
import threading

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

    valid = threading.Thread(target=validation , args=(admin.id,))
    valid.start()
    
    return (str(admin.id), 201)

def validation(user_id):
    user = db.session.query(Order).filter(Order.id == user_id).first()
    if user.age > 18 and user.credit < 100000:
        user.status = True
    else:
        user.status = False

    db.session.add(user)
    db.session.commit()
    


@app.route("/credit/<int:post_id>", methods=["GET"])
def get(post_id):
    user = db.session.query(Order).filter(Order.id == post_id).first()
    if user.status is True:
        return "Approved"
    else:
        return "Denied"


    # orders = Order.query.all()
    # # data = []

    # for order in orders:
    #     data.append({
    #         "name": order.name,
    #         "age": order.age,
    #         "credit": order.credit
    #     })
    # return (json.dumps(data), 200)


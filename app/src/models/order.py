from config import db
import threading

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    credit = db.Column(db.Float, nullable=False)
    status = db.Column(db.Boolean, nullable=True)

def add_user(body):
    admin = Order( 
                name = body["name"],
                age = body["age"],
                credit = body["credit"] 
            )
    db.session.add(admin)
    db.session.commit()
    start_validation(admin)
    return admin
    

def start_validation(admin):
    valid = threading.Thread(target = validation , args=(admin.id,))
    valid.start()

def validation(user_id):
    user = db.session.query(Order).filter(Order.id == user_id).first()
    if user.age > 18 and user.credit < 100000:
        user.status = True
        print({user.name : "Approved!"}, flush=True)
    else:
        print({user.name : "Denied!"}, flush=True)
        user.status = False
    db.session.add(user)
    db.session.commit()



def show_all():
    orders = Order.query.all()
    data = list()

    for order in orders:
        data.append({
            "ticket": order.id,
            "name": order.name,
            "age": order.age,
            "credit": order.credit,
            "status": order.status
        })
    print(data, flush=True)
    return data

def data_user(post_id):
    data =  db.session.query(Order).filter(Order.id == post_id).first()
    return data

db.create_all()
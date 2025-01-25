from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

app = Flask(__name__)
CORS(app)

db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db"
db.init_app(app)

class User(db.Model):
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    user_id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)

class Task(db.Model):
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    task_id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50))
    task_content = db.Column(db.String(50))
    date_due = db.Column(db.String(50)) # mm/dd/yyyy
    task_tag = db.Column(db.String(50))
    status = db.Column(db.Boolean)
    xp_cost = db.Column(db.Integer)

with app.app_context():
    db.create_all()

@app.route("/user/<username>/info")
def getInfo(username):
    userInfo = db.one_or_404(db.select(User).filter_by(username=username)).as_dict()
    tasks = getAllTasks(userInfo["user_id"])[0].get_json()
    print(tasks)
    print(type(tasks))
    response = {"user": userInfo, "tasks": tasks}
    return jsonify(response), 200

@app.route("/user/<user_id>", methods=["GET"])
def getUser(user_id):
    info = db.get_or_404(User, user_id).as_dict()
    return jsonify(info), 200

@app.route("/user/create", methods=["POST"])
def createUser():
    req = request.get_json()
    user = User(
        user_id = req["user_id"],
        username = req["username"],
        email = req["email"],
    )
    db.session.add(user)
    db.session.commit()
    return jsonify("User added"), 200

@app.route("/user/<user_id>/delete", methods=["POST"])
def deleteUser(user_id):
    user = db.get_or_404(User, user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify("User deleted"), 200

@app.route("/user/deleteAll", methods=["POST"])
def deleteAllUsers():
    try:
        db.session.query(User).delete()
        db.session.commit()
    except:
        db.session.rollback()
    return jsonify("All Users deleted"), 200

@app.route("/task/<user_id>/collect", methods=["GET"])
def getAllTasks(user_id):
    tasks = db.session.execute(db.select(Task).filter_by(user_id=user_id)).scalars()
    response = [i.as_dict() for i in tasks]
    return jsonify(response), 200

@app.route("/task/<task_id>", methods=["GET"])
def getTask(task_id):
    info = db.get_or_404(Task, task_id).as_dict()
    return jsonify(info), 200

@app.route("/task/create", methods=["POST"])
def createTask():
    req = request.get_json()
    task = Task(
        task_id = req["task_id"],
        user_id = req["user_id"],
        task_content = req["task_content"],
        date_due = req["date_due"],
        task_tag = req["task_tag"],
        status = req["status"],
        xp_cost = req["xp_cost"],
    )
    db.session.add(task)
    db.session.commit()
    return jsonify("Task added"), 200

@app.route("/task/<task_id>/delete", methods=["POST"])
def deleteTask(task_id):
    task = db.get_or_404(Task, task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify("Task deleted"), 200

@app.route("/task/deleteAll", methods=["POST"])
def deleteAllTasks():
    try:
        db.session.query(Task).delete()
        db.session.commit()
    except:
        db.session.rollback()
    return jsonify("All Task deleted"), 200

if __name__ == "__main__":
    app.run(debug=True)

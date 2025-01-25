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

@app.route("/info/<user_id>", methods=["GET"])
def info(user_id):
    info = db.get_or_404(User, user_id).as_dict()
    print(info)
    return jsonify(info), 200

@app.route("/newUser", methods=["POST"])
def newUser():
    req = request.get_json()
    user = User(
        user_id = req["user_id"],
        username = req["username"],
        email = req["email"],
    )
    db.session.add(user)
    db.session.commit()
    return jsonify("User added"), 200

if __name__ == "__main__":
    app.run(debug=True)

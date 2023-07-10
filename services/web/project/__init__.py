from dataclasses import dataclass
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('project.config.Config')
db = SQLAlchemy(app)


@dataclass
class User(db.Model):
    id: int
    email: str
    active: bool

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email


@app.get('/')
def read_root():
    users = User.query.all()
    return jsonify([{"id": user.id, "email": user.email} for user in users])

from app import db
from flask_login import UserMixin
from datetime import datetime
flask db migrate -m "Atualização de modelos"
flask db upgrade

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    videos = db.relationship('Video', backref='author', lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"

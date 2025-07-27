# C:\Users\clove\Documents\viral_video_app\app\models\user.py

from app import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    profile_image = db.Column(db.String(20), nullable=False, default='default.jpg')

    # AQUI ESTÁ A ALTERAÇÃO: Mude 'lazy=True' para 'lazy='dynamic''
    videos = db.relationship('Video', backref='author', lazy='dynamic') # <-- MODIFICADO

    def __repr__(self):
        return f"<User {self.username}>"

# Se a classe Video estiver no app/models/video.py, você pode precisar importá-la aqui
# se o modelo User fizer referência direta a ela (como no db.relationship).
# No entanto, backref geralmente lida com isso.
# Certifique-se que Video também importa db de 'app'.
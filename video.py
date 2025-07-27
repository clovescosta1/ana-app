# C:\Users\clove\Documents\viral_video_app\app\models\video.py
from datetime import datetime
from app import db # Necessário para db.Model

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, default="Vídeo Sem Título")
    description = db.Column(db.Text, nullable=True)
    file_path = db.Column(db.String(255), nullable=False)
    thumbnail_path = db.Column(db.String(255), nullable=True) # Caminho para a thumbnail
    uploaded_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    views = db.Column(db.Integer, default=0)
    status = db.Column(db.String(20), default='pending') # Ex: 'pending', 'processed', 'failed'

    # Chave estrangeira para o usuário que enviou o vídeo
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Video('{self.title}', '{self.uploaded_at}', '{self.status}')"
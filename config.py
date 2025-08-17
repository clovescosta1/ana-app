# C:\Users\clove\Documents\viral_video_app\config.py

import os

# Caminho para o executável do ImageMagick
IMAGEMAGICK_BINARY_PATH = r"C:\Program Files\ImageMagick-7.1.1-Q16\magick.exe"  # <--- AJUSTE CONFORME SEU SISTEMA

# Chave Secreta (Sessões, CSRF, etc.)
# É CRÍTICO que esta chave seja ÚNICA e SECRETA.
SECRET_KEY = os.environ.get('SECRET_KEY') or 'sua-chave-secreta-altamente-complexa-e-unica-aqui'

# Configuração do Banco de Dados SQLAlchemy
# DATABASE_URL pode ser definida como uma variável de ambiente
# Exemplo: postgresql://user:pass@host:port/db
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')

# Desativa o rastreamento de modificações de objetos do SQLAlchemy
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configurações para Celery e Redis
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL') or 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND') or 'redis://localhost:6379/0'

# Diga ao Celery onde encontrar suas tarefas
# Se as tarefas estão em app/tasks.py, use 'app.tasks'
CELERY_IMPORTS = ('app.tasks',)

# ==========================
# 🔑 Configurações de Domínio e CORS
# ==========================

# URL base do aplicativo (Render vai definir essa variável)
APP_BASE_URL = os.environ.get("APP_BASE_URL", "http://localhost:5000")

# Lista de domínios permitidos para CORS (separados por vírgula)
# Exemplo no Render: 
# CORS_ORIGINS = https://jcdicaseconhecimentos.com.br,https://painel-ana.jcdicaseconhecimentos.com.br
CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "*").split(",")

# ==========================
# 🔧 Outras integrações externas (opcional)
# ==========================
# OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
# CLOUDINARY_CLOUD_NAME = os.environ.get('CLOUDINARY_CLOUD_NAME')
# CLOUDINARY_API_KEY = os.environ.get('CLOUDINARY_API_KEY')
# CLOUDINARY_API_SECRET = os.environ.get('CLOUDINARY_API_SECRET')

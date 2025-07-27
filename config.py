# C:\Users\clove\Documents\viral_video_app\config.py

import os

# Define o diretório base do seu projeto
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Classe base para configurações do aplicativo Flask."""
    # AQUI ESTÁ A CORREÇÃO CRÍTICA PARA O IMAGEMAGICK
    # Agora apontando diretamente para o executável magick.exe
    IMAGEMAGICK_BINARY_PATH = r"C:\Program Files\ImageMagick-7.1.1-Q16\magick.exe" # <--- AJUSTADO PARA O SEU CAMINHO REAL E EXECUTÁVEL!

    # Chave Secreta: Usada para segurança (sessões, CSRF, etc.)
    # É CRÍTICO que esta chave seja ÚNICA e SECRETA.
    # Use uma string complexa ou uma variável de ambiente.
    # Exemplo: import secrets; secrets.token_hex(16)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sua-chave-secreta-altamente-complexa-e-unica-aqui'

    # Configuração do Banco de Dados SQLAlchemy
    # DATABASE_URL pode ser definida como uma variável de ambiente (ex: postgresql://user:pass@host:port/db)
    # Se não definida, usa um banco de dados SQLite local (app.db)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    # Desativa o rastreamento de modificações de objetos do SQLAlchemy para economizar recursos.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configurações para Celery e Redis
    # CELERY_BROKER_URL é o endereço do seu broker (Redis neste caso)
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL') or 'redis://localhost:6379/0'
    # CELERY_RESULT_BACKEND é onde os resultados das tarefas do Celery são armazenados (Redis)
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND') or 'redis://localhost:6379/0'

    # ADICIONADO: Diga ao Celery onde encontrar suas tarefas
    # Aponta para o módulo específico onde a tarefa generate_video_task está definida
    # Se a tarefa 'generate_video_task' está dentro de 'app/tasks.py', então é 'app.tasks'.
    # Se estivesse em 'app/tasks/meutarefas.py', seria 'app.tasks.meutarefas'.
    # Baseado nos logs, 'app.tasks' parece ser o correto.
    CELERY_IMPORTS = ('app.tasks',) # <--- CORREÇÃO: Removido '.generate_video_task' se 'tasks' é um módulo diretamente.

    # Adicione outras configurações específicas do seu aplicativo aqui
    # Por exemplo, chaves de API para serviços externos (OpenAI, etc.)
    # OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    # CLOUDINARY_CLOUD_NAME = os.environ.get('CLOUDINARY_CLOUD_NAME')
    # CLOUDINARY_API_KEY = os.environ.get('CLOUDINARY_API_KEY')
    # CLOUDINARY_API_SECRET = os.environ.get('CLOUDINARY_API_SECRET')
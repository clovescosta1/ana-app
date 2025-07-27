# app/celery_app.py
from celery import Celery

# Crie uma instância Celery vazia por enquanto.
# Ela será configurada com as settings do Flask mais tarde.
celery_app = Celery('viral_video_app')

# Esta função será usada para configurar a instância 'celery_app'
# com as configurações do Flask, incluindo o contexto da aplicação.
def init_celery(app):
    # Use as configurações do Flask para o Celery
    app.config.setdefault('CELERY_BROKER_URL', 'redis://localhost:6379/0')
    app.config.setdefault('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')

    celery_app.conf.update(
        broker_url=app.config['CELERY_BROKER_URL'],
        result_backend=app.config['CELERY_RESULT_BACKEND'],
        task_track_started=True,
        timezone='America/Sao_Paulo',
        result_expires=3600,
        broker_connection_retry_on_startup=True
    )

    # Autodiscover tasks
    # Assegure-se de que o Celery encontre suas tarefas em 'app.tasks'
    celery_app.autodiscover_tasks(['app.tasks'])

    # Crie uma Task personalizada que roda dentro do contexto da aplicação Flask
    class ContextTask(celery_app.Task):
        def __call__(self, *args, **kwargs):
            # Crie um novo contexto de aplicação para cada execução de tarefa
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app.Task = ContextTask
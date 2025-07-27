# C:\Users\clove\Documents\viral_video_app\app\tasks\generate_video_task.py

import os
import logging
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip, TextClip, ColorClip
from app.models.video import Video
from app import db # Importar db
from app import celery_app # <--- CORRIGIDO: Importar celery_app de 'app'
from app import create_app

logger = logging.getLogger(__name__)

@celery_app.task
def generate_video_task(video_id):
    # Cria um contexto de aplicação Flask para que o SQLAlchemy funcione dentro da tarefa
    app = create_app() # create_app() é do app/__init__.py
    with app.app_context():
        logger.info(f"Iniciando a tarefa de geração de vídeo para o ID: {video_id}")
        video = Video.query.get(video_id)
        if not video:
            logger.error(f"Vídeo com ID {video_id} não encontrado.")
            return

        try:
            output_dir_videos = os.path.join('app', 'static', 'uploads', 'videos')
            output_dir_thumbnails = os.path.join('app', 'static', 'uploads', 'thumbnails')

            os.makedirs(output_dir_videos, exist_ok=True)
            os.makedirs(output_dir_thumbnails, exist_ok=True)

            output_filename = f"video_{video.id}.mp4"
            output_filepath = os.path.join(output_dir_videos, output_filename)

            logger.info(f"Caminho de saída do vídeo: {output_filepath}")

            clip = ColorClip(size=(1280, 720), color=(0,0,0), duration=5)
            txt_clip = TextClip(f"Tema: {video.title}", fontsize=70, color='white', bg_color='blue')
            txt_clip = txt_clip.set_pos("center").set_duration(5)
            final_clip = CompositeVideoClip([clip, txt_clip])

            logger.info("Tentando escrever o arquivo de vídeo...")
            final_clip.write_videofile(output_filepath, fps=24, threads=4)

            logger.info(f"Vídeo {output_filename} gerado com sucesso!")

            video.status = 'concluido'
            video.file_path = output_filename
            db.session.commit()
            logger.info(f"Status do vídeo {video.id} atualizado para 'concluido'.")

        except Exception as e:
            db.session.rollback()
            video.status = 'falha'
            db.session.commit()
            logger.error(f"Erro ao gerar vídeo {video_id}: {e}", exc_info=True)
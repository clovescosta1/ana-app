from flask import render_template, request, jsonify, Blueprint, send_file, url_for
from flask_login import login_required, current_user
from app.services.groq_service import gerar_roteiro_viral
from app.services.jcsshop_service import buscar_noticias, gerar_tema_do_dia
from app.services.video_service import gerar_video_completo
import os

video_bp = Blueprint('video', __name__)

VIDEOS_DIR = os.path.join(os.path.dirname(__file__), '..', 'static', 'videos')

@video_bp.route('/gerar-video', methods=['GET'])
@login_required
def gerar_video():
    noticias = buscar_noticias()
    tema_sugerido = gerar_tema_do_dia()
    return render_template('video/gerar_video.html',
                         noticias=noticias,
                         tema_sugerido=tema_sugerido)

@video_bp.route('/gerar-roteiro', methods=['POST'])
@login_required
def gerar_roteiro():
    tema = request.form.get('tema', '')
    plataforma = request.form.get('plataforma', 'instagram')
    usar_jcsshop = request.form.get('usar_jcsshop', 'false')

    dados_mercado = ""
    if usar_jcsshop == 'true':
        noticias = buscar_noticias()
        dados_mercado = "\n".join(noticias)

    roteiro = gerar_roteiro_viral(tema, dados_mercado, plataforma)
    return jsonify(roteiro)

@video_bp.route('/criar-video', methods=['POST'])
@login_required
def criar_video():
    """Gera o arquivo de vídeo a partir do roteiro."""
    data = request.get_json()
    roteiro = data.get('roteiro', {})
    plataforma = data.get('plataforma', 'instagram')

    try:
        nome_video = gerar_video_completo(roteiro, plataforma)
        if nome_video:
            url = url_for('static', filename=f'videos/{nome_video}')
            return jsonify({"sucesso": True, "url": url, "nome": nome_video})
        else:
            return jsonify({"sucesso": False, "erro": "Falha ao gerar vídeo"})
    except Exception as e:
        return jsonify({"sucesso": False, "erro": str(e)})

@video_bp.route('/meus-videos', methods=['GET'])
@login_required
def meus_videos():
    videos = []
    if os.path.exists(VIDEOS_DIR):
        for f in os.listdir(VIDEOS_DIR):
            if f.endswith('.mp4'):
                videos.append(f)
    return render_template('video/meus_videos.html', videos=videos)

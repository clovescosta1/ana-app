from flask import render_template, request, jsonify, Blueprint, flash, redirect, url_for
from flask_login import login_required, current_user
from app.services.groq_service import gerar_roteiro_viral
from app.services.jcsshop_service import buscar_noticias, gerar_tema_do_dia

video_bp = Blueprint('video', __name__)

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

@video_bp.route('/meus-videos', methods=['GET'])
@login_required
def meus_videos():
    return render_template('video/meus_videos.html')

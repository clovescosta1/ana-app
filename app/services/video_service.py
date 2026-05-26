from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import uuid
import textwrap

try:
    from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips, CompositeAudioClip
    MOVIEPY_OK = True
except:
    MOVIEPY_OK = False

try:
    from gtts import gTTS
    GTTS_OK = True
except:
    GTTS_OK = False

VIDEOS_DIR = os.path.join(os.path.dirname(__file__), '..', 'static', 'videos')
os.makedirs(VIDEOS_DIR, exist_ok=True)

CORES = {
    'fundo': '#0f0f1a',
    'dourado': '#d4af37',
    'branco': '#ffffff',
    'cinza': '#aaaaaa',
    'verde': '#00ff88',
    'vermelho': '#ff4444'
}

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def criar_slide(titulo, texto, subtitulo="", tipo="normal", largura=1080, altura=1920):
    """Cria um slide como imagem numpy."""
    fundo_rgb = hex_to_rgb(CORES['fundo'])
    img = Image.new('RGB', (largura, altura), color=fundo_rgb)
    draw = ImageDraw.Draw(img)

    # Gradiente de fundo (simulado)
    for i in range(100):
        alpha = int(30 * (1 - i/100))
        draw.rectangle([0, i*2, largura, i*2+2], 
                       fill=(hex_to_rgb(CORES['dourado'])[0], 
                             hex_to_rgb(CORES['dourado'])[1], 
                             hex_to_rgb(CORES['dourado'])[2]))

    # Fundo principal
    draw.rectangle([0, 0, largura, altura], fill=fundo_rgb)

    # Barra dourada topo
    draw.rectangle([0, 0, largura, 10], fill=hex_to_rgb(CORES['dourado']))
    # Barra dourada base
    draw.rectangle([0, altura-10, largura, altura], fill=hex_to_rgb(CORES['dourado']))

    # Logo JCSSHOP pequeno
    try:
        font_logo = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
    except:
        font_logo = ImageFont.load_default()
    draw.text((50, 40), "JCSSHOP", fill=hex_to_rgb(CORES['dourado']), font=font_logo)
    draw.text((largura-200, 40), "AnaSync IA", fill=hex_to_rgb(CORES['cinza']), font=font_logo)

    # Linha separadora
    draw.rectangle([50, 100, largura-50, 104], fill=hex_to_rgb(CORES['dourado']))

    # Fonte principal
    try:
        font_titulo = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 72)
        font_texto = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 52)
        font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 42)
    except:
        font_titulo = ImageFont.load_default()
        font_texto = font_titulo
        font_sub = font_titulo

    # Título em dourado
    y_pos = 200
    if titulo:
        linhas_titulo = textwrap.wrap(titulo, width=18)
        for linha in linhas_titulo:
            bbox = draw.textbbox((0, 0), linha, font=font_titulo)
            w = bbox[2] - bbox[0]
            draw.text(((largura - w) // 2, y_pos), linha, 
                     fill=hex_to_rgb(CORES['dourado']), font=font_titulo)
            y_pos += 90

    y_pos += 40

    # Linha decorativa
    draw.rectangle([largura//4, y_pos, 3*largura//4, y_pos+4], 
                   fill=hex_to_rgb(CORES['dourado']))
    y_pos += 40

    # Texto principal em branco
    if texto:
        linhas_texto = textwrap.wrap(texto, width=22)
        for linha in linhas_texto[:8]:  # max 8 linhas
            bbox = draw.textbbox((0, 0), linha, font=font_texto)
            w = bbox[2] - bbox[0]
            draw.text(((largura - w) // 2, y_pos), linha,
                     fill=hex_to_rgb(CORES['branco']), font=font_texto)
            y_pos += 75

    # Subtítulo em cinza
    if subtitulo:
        y_pos += 30
        linhas_sub = textwrap.wrap(subtitulo, width=28)
        for linha in linhas_sub[:3]:
            bbox = draw.textbbox((0, 0), linha, font=font_sub)
            w = bbox[2] - bbox[0]
            draw.text(((largura - w) // 2, y_pos), linha,
                     fill=hex_to_rgb(CORES['cinza']), font=font_sub)
            y_pos += 55

    # Rodapé
    rodape = "jcsshop.com.br | Inteligência Financeira"
    try:
        font_rodape = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 34)
    except:
        font_rodape = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), rodape, font=font_rodape)
    w = bbox[2] - bbox[0]
    draw.text(((largura - w) // 2, altura - 70), rodape,
             fill=hex_to_rgb(CORES['cinza']), font=font_rodape)

    return np.array(img)

def gerar_audio(texto, nome_arquivo):
    """Gera áudio em português usando gTTS."""
    if not GTTS_OK:
        return None
    try:
        tts = gTTS(text=texto, lang='pt', slow=False)
        caminho = os.path.join(VIDEOS_DIR, nome_arquivo)
        tts.save(caminho)
        return caminho
    except Exception as e:
        print(f"Erro gTTS: {e}")
        return None

def gerar_video_completo(roteiro: dict, plataforma: str = "instagram") -> str:
    """
    Gera vídeo completo a partir do roteiro.
    Retorna o caminho do arquivo gerado.
    """
    if not MOVIEPY_OK:
        return None

    video_id = str(uuid.uuid4())[:8]
    
    # Configuração por plataforma
    config = {
        "instagram": {"w": 1080, "h": 1920, "fps": 30},
        "tiktok":    {"w": 1080, "h": 1920, "fps": 30},
        "youtube":   {"w": 1920, "h": 1080, "fps": 30},
        "facebook":  {"w": 1280, "h": 720,  "fps": 30},
    }
    cfg = config.get(plataforma, config["instagram"])

    # Montar slides do roteiro
    slides_dados = [
        {
            "titulo": "ATENÇÃO!",
            "texto": roteiro.get("gancho", ""),
            "duracao": 4
        },
        {
            "titulo": "SAIBA MAIS",
            "texto": roteiro.get("desenvolvimento", "")[:200],
            "duracao": 8
        },
        {
            "titulo": "CONCLUSÃO",
            "texto": roteiro.get("cta", ""),
            "duracao": 4
        },
        {
            "titulo": "SIGA AGORA",
            "texto": "@jcsshop24\njcsshop.com.br",
            "subtitulo": "Inteligência Financeira com IA",
            "duracao": 3
        }
    ]

    clips = []
    texto_naracao = ""

    for i, slide in enumerate(slides_dados):
        frame = criar_slide(
            titulo=slide.get("titulo", ""),
            texto=slide.get("texto", ""),
            subtitulo=slide.get("subtitulo", ""),
            largura=cfg["w"],
            altura=cfg["h"]
        )
        clip = ImageClip(frame).set_duration(slide["duracao"])
        clips.append(clip)
        texto_naracao += " " + slide.get("texto", "")

    # Concatenar clips
    from moviepy.editor import concatenate_videoclips
    video_final = concatenate_videoclips(clips, method="compose")

    # Gerar áudio de narração
    audio_path = gerar_audio(texto_naracao[:500], f"audio_{video_id}.mp3")
    if audio_path and os.path.exists(audio_path):
        try:
            audio = AudioFileClip(audio_path)
            # Ajustar duração do áudio ao vídeo
            duracao_video = video_final.duration
            if audio.duration > duracao_video:
                audio = audio.subclip(0, duracao_video)
            video_final = video_final.set_audio(audio)
        except Exception as e:
            print(f"Erro ao adicionar áudio: {e}")

    # Salvar vídeo
    nome_video = f"video_{video_id}.mp4"
    caminho_video = os.path.join(VIDEOS_DIR, nome_video)
    
    video_final.write_videofile(
        caminho_video,
        fps=cfg["fps"],
        codec='libx264',
        audio_codec='aac',
        verbose=False,
        logger=None
    )

    return nome_video

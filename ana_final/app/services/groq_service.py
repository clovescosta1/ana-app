import os
import requests
import json
import re

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

def gerar_roteiro_viral(tema: str, dados_mercado: str = "", plataforma: str = "instagram") -> dict:

    instrucoes = {
        "instagram": """
Você é um especialista em conteúdo viral para Instagram Reels.
Crie roteiros que:
- Começam com GANCHO nos primeiros 3 segundos (pergunta ou afirmação impactante)
- Usam linguagem direta e simples
- Têm ritmo rápido (cortes a cada 2-3 segundos)
- Terminam com CTA claro (salvar, compartilhar, seguir)
- Duração ideal: 30-60 segundos
- Use emojis estrategicamente
""",
        "tiktok": """
Você é um especialista em conteúdo viral para TikTok.
Crie roteiros que:
- GANCHO explosivo nos primeiros 1-2 segundos
- Tendências atuais e sons populares
- Storytelling rápido e envolvente
- Texto na tela sincronizado com fala
- Duração ideal: 15-45 segundos
- Tom jovem, autêntico e dinâmico
""",
        "facebook": """
Você é um especialista em conteúdo viral para Facebook.
Crie roteiros que:
- Começam com informação de valor imediata
- Geram discussão e comentários
- Compartilháveis para grupos de investimento
- Duração ideal: 1-3 minutos
- Tom mais formal mas acessível
""",
        "youtube": """
Você é um especialista em conteúdo viral para YouTube.
Crie roteiros que:
- Título otimizado para SEO com palavra-chave principal
- GANCHO nos primeiros 30 segundos (problema + promessa de solução)
- Estrutura: Intro → Desenvolvimento em tópicos → Conclusão → CTA
- Linguagem conversacional e didática
- Duração ideal: 8-15 minutos (maximiza watch time e receita)
- Descrição otimizada com timestamps e palavras-chave
- Tags relevantes para o algoritmo
- Thumbnail descrita (cores, texto, expressão)
- Inclua momentos de retenção (perguntas, cliffhangers)
"""
    }

    prompt = f"""
{instrucoes.get(plataforma, instrucoes['instagram'])}

TEMA DO VÍDEO: {tema}

DADOS DO MERCADO (use se relevante):
{dados_mercado}

Gere um roteiro completo com:
1. GANCHO (primeiros segundos/minutos)
2. DESENVOLVIMENTO (corpo do vídeo com tópicos)
3. CTA (call to action final)
4. LEGENDA/DESCRIÇÃO completa com hashtags
5. DESCRIÇÃO das cenas/imagens sugeridas
{"6. TÍTULO SEO otimizado" if plataforma == "youtube" else ""}
{"7. TAGS para YouTube (20 tags relevantes)" if plataforma == "youtube" else ""}
{"8. THUMBNAIL (descrição visual detalhada)" if plataforma == "youtube" else ""}

Responda APENAS com JSON válido, sem texto antes ou depois, com as chaves:
gancho, desenvolvimento, cta, legenda, cenas{"titulo, tags, thumbnail" if plataforma == "youtube" else ""}
"""

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.8,
        "max_tokens": 3000
    }

    try:
        response = requests.post(GROQ_URL, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        conteudo = data["choices"][0]["message"]["content"]

        json_match = re.search(r'\{.*\}', conteudo, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        else:
            return {
                "gancho": conteudo[:200],
                "desenvolvimento": conteudo[200:600],
                "cta": "Curta, comente e se inscreva!",
                "legenda": tema,
                "cenas": "Vídeo dinâmico com textos na tela"
            }
    except Exception as e:
        return {"erro": str(e)}

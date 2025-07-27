import os
from pathlib import Path

# Defina a estrutura do seu aplicativo Flask aqui
# 'None' indica um arquivo, e um dicionário indica um diretório
PROJECT_ROOT = "my_flask_app"
FLASK_STRUCTURE = {
    "app": {
        "static": {
            "css": {
                "style.css": None
            },
            "js": None,
            "images": None
        },
        "templates": {
            "base.html": None,
            "index.html": None
        },
        "blueprints": {
            "__init__.py": None,
            "home.py": None
        },
        "__init__.py": None,
        "models.py": None
    },
    "config.py": None,
    "run.py": None,
    ".env": None,
    "requirements.txt": None
}

def create_structure(base_path, structure):
    """
    Função recursiva para criar a estrutura de diretórios e arquivos.
    """
    for name, content in structure.items():
        current_path = Path(base_path) / name
        if content is None:  # É um arquivo
            try:
                current_path.touch()
                # AINDA SEM LOG BONITO:
                print(f"[CRIADO] Arquivo: {current_path}")
            except Exception as e:
                print(f"[ERRO] Ao criar arquivo {current_path}: {e}")
        else:  # É um diretório
            try:
                current_path.mkdir(exist_ok=True)
                # AINDA SEM LOG BONITO:
                print(f"[CRIADO] Diretório: {current_path}")
                create_structure(current_path, content) # Recursão para subdiretórios
            except Exception as e:
                print(f"[ERRO] Ao criar diretório {current_path}: {e}")

# --- Ponto de entrada do script ---
if __name__ == "__main__":
    print(f"Iniciando a criação da estrutura do projeto '{PROJECT_ROOT}'...")
    
    # Cria o diretório raiz do projeto se não existir
    Path(PROJECT_ROOT).mkdir(exist_ok=True)
    
    create_structure(PROJECT_ROOT, FLASK_STRUCTURE)
    
    print("\nEstrutura criada com sucesso!")
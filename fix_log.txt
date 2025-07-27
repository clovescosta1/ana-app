import os

# Caminho base do seu projeto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Função para garantir que existe __init__.py nas pastas
def ensure_init_files():
    print("\n🔧 Verificando __init__.py...")
    folders = ['app', 'app/auth', 'app/main']
    for folder in folders:
        path = os.path.join(BASE_DIR, folder, '__init__.py')
        if not os.path.exists(path):
            with open(path, 'w') as f:
                f.write('# Arquivo criado automaticamente\n')
            print(f'✅ Criado: {path}')
        else:
            print(f'✔️ Já existe: {path}')

# Função para corrigir run.py
def fix_run_py():
    print("\n🔧 Corrigindo run.py...")
    run_path = os.path.join(BASE_DIR, 'run.py')
    content = """from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
"""
    with open(run_path, 'w') as f:
        f.write(content)
    print(f'✅ run.py corrigido com sucesso')

# Função para corrigir __init__.py principal
def fix_init_py():
    print("\n🔧 Corrigindo app/__init__.py...")
    init_path = os.path.join(BASE_DIR, 'app', '__init__.py')
    content = """from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.auth.routes import auth_bp
    from app.main.routes import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app
"""
    with open(init_path, 'w') as f:
        f.write(content)
    print('✅ app/__init__.py corrigido')

# Função para criar Blueprints básicos
def create_blueprint(folder, name):
    print(f"\n🔧 Verificando Blueprint: {folder}/routes.py...")
    path = os.path.join(BASE_DIR, 'app', folder, 'routes.py')
    if not os.path.exists(path):
        content = f"""from flask import Blueprint

{name}_bp = Blueprint('{name}', __name__, url_prefix='/{name}')

@{name}_bp.route('/')
def index():
    return 'Página {name} funcionando'
"""
        with open(path, 'w') as f:
            f.write(content)
        print(f'✅ Blueprint {folder} criado')
    else:
        print(f'✔️ Blueprint {folder} já existe')

# Função para corrigir requirements.txt
def fix_requirements():
    print("\n🔧 Corrigindo requirements.txt...")
    req_path = os.path.join(BASE_DIR, 'requirements.txt')
    if not os.path.exists(req_path):
        print("⚠️ requirements.txt não encontrado")
        return

    with open(req_path, 'r') as f:
        lines = f.readlines()

    corrected_lines = []
    for line in lines:
        parts = line.strip().split('==')
        if len(parts) > 2:
            # Quebra linhas coladas
            for part in line.strip().split('=='):
                if part.strip():
                    corrected_lines.append(part.strip() + '\n')
        else:
            corrected_lines.append(line if line.endswith('\n') else line + '\n')

    with open(req_path, 'w') as f:
        f.writelines(corrected_lines)

    print("✅ requirements.txt corrigido")

# Executar as funções
if __name__ == '__main__':
    ensure_init_files()
    fix_run_py()
    fix_init_py()
    create_blueprint('auth', 'auth')
    create_blueprint('main', 'main')
    fix_requirements()
    print("\n🎯 Projeto corrigido e pronto para rodar!")

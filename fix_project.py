import os
import ast
import re
import subprocess

# Caminho base do projeto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 🔧 Logger simples
def log(msg):
    with open(os.path.join(BASE_DIR, 'fix_log.txt'), 'a', encoding='utf-8') as log_file:
        log_file.write(msg + '\n')
    print(msg)


#################################
# 🔥 Remover BOM (Byte Order Mark)
#################################
def remove_bom(file_path):
    try:
        with open(file_path, 'rb') as f:
            content = f.read()

        if content.startswith(b'\xef\xbb\xbf'):
            log(f'🩹 Removendo BOM de {file_path}')
            content = content[3:]
            with open(file_path, 'wb') as f:
                f.write(content)
        else:
            log(f'✔️ Sem BOM: {file_path}')
    except Exception as e:
        log(f'⚠️ Erro ao remover BOM de {file_path}: {e}')


#################################
# 🧠 Checagem de Sintaxe
#################################
def check_syntax(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            source = file.read()
        ast.parse(source, filename=file_path)
        log(f"✔️ Sem erros de sintaxe: {file_path}")
        return True
    except SyntaxError as e:
        log(f"❌ Erro de sintaxe em {file_path}: {e}")
        return False
    except Exception as e:
        log(f"⚠️ Erro ao verificar {file_path}: {e}")
        return False


#################################
# 🔧 Garantir __init__.py nas pastas
#################################
def ensure_init_files():
    log("\n🔧 Verificando __init__.py...")
    folders = ['app', 'app/auth', 'app/main', 'app/templates', 'app/static']
    for folder in folders:
        path = os.path.join(BASE_DIR, folder, '__init__.py')
        if not os.path.exists(path):
            with open(path, 'w') as f:
                f.write('# Criado automaticamente\n')
            log(f'✅ Criado: {path}')
        else:
            log(f'✔️ Já existe: {path}')


#################################
# 🏃 Corrigir run.py
#################################
def fix_run_py():
    log("\n🔧 Corrigindo run.py...")
    run_path = os.path.join(BASE_DIR, 'run.py')
    content = """from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
"""
    with open(run_path, 'w', encoding='utf-8') as f:
        f.write(content)
    log('✅ run.py corrigido')


#################################
# 🔥 Corrigir app/__init__.py
#################################
def fix_init_py():
    log("\n🔧 Corrigindo app/__init__.py...")
    init_path = os.path.join(BASE_DIR, 'app', '__init__.py')
    content = """from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    from app.auth.routes import auth_bp
    from app.main.routes import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    @app.errorhandler(404)
    def not_found(e):
        return render_template('404.html'), 404

    return app
"""
    with open(init_path, 'w', encoding='utf-8') as f:
        f.write(content)
    log('✅ app/__init__.py corrigido')


#################################
# 🔧 Criar config.py
#################################
def create_config():
    log("\n🔧 Criando config.py...")
    path = os.path.join(BASE_DIR, 'app', 'config.py')
    content = """import os

SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key_here'
"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    log('✅ config.py criado')


#################################
# 🔖 Corrigir ou criar Blueprints
#################################
def create_blueprint(folder, name):
    log(f"\n🔧 Verificando Blueprint: {folder}/routes.py...")
    path = os.path.join(BASE_DIR, 'app', folder, 'routes.py')
    if not os.path.exists(path):
        content = f"""from flask import Blueprint, render_template

{name}_bp = Blueprint('{name}', __name__, url_prefix='/{name}')

@{name}_bp.route('/')
def index():
    return render_template('{name}/index.html')
"""
        os.makedirs(os.path.join(BASE_DIR, 'app', 'templates', name), exist_ok=True)
        html_path = os.path.join(BASE_DIR, 'app', 'templates', name, 'index.html')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(f"<h1>Página {name} funcionando</h1>")
        log(f'✅ Blueprint {folder} criado')
    else:
        log(f'✔️ Blueprint {folder} já existe')


#################################
# 🔧 Criar página 404
#################################
def create_error_page():
    log("\n🔧 Criando página 404...")
    path = os.path.join(BASE_DIR, 'app', 'templates', '404.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write("<h1>404 - Página não encontrada</h1>")
    log('✅ Página 404 criada')


#################################
# 📦 Corrigir requirements.txt
#################################
def fix_requirements():
    log("\n🔧 Corrigindo requirements.txt...")
    req_path = os.path.join(BASE_DIR, 'requirements.txt')
    if not os.path.exists(req_path):
        log("⚠️ requirements.txt não encontrado")
        return

    with open(req_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    corrected_lines = []
    for line in lines:
        line = line.strip()
        if '==' in line and line.count('==') > 1:
            parts = re.split(r'(?<==)=', line)
            for part in parts:
                if part.strip():
                    corrected_lines.append(part.strip() + '\n')
        elif line:
            corrected_lines.append(line + '\n')

    with open(req_path, 'w', encoding='utf-8') as f:
        f.writelines(corrected_lines)

    log("✅ requirements.txt corrigido")


#################################
# 🔧 Verificar se Flask está instalado
#################################
def check_flask():
    try:
        import flask
        log("✔️ Flask instalado")
    except ImportError:
        log("❌ Flask não instalado. Instalando...")
        subprocess.call(["pip", "install", "flask"])


#################################
# 🧠 Checar sintaxe e BOM em todos .py
#################################
def syntax_check_all():
    log("\n🧠 Fazendo checagem de sintaxe e BOM...")
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith('.py'):
                path = os.path.join(root, file)
                remove_bom(path)
                check_syntax(path)


#################################
# 🚀 Execução principal (única vez)
#################################
if __name__ == '__main__':
    log("\n🚀 Iniciando Fix Project (execução única)")

    check_flask()
    ensure_init_files()
    fix_run_py()
    fix_init_py()
    create_config()
    create_blueprint('auth', 'auth')
    create_blueprint('main', 'main')
    create_error_page()
    fix_requirements()
    syntax_check_all()

    log("\n✅ Correção concluída! O script finalizou.\n")

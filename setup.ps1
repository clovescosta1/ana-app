# Caminho do ambiente virtual[flake8]
exclude = .git, __pycache__, env, venv, .venv, build, dist, migrations
max-line-length = 120
$venvPath = ".\venv\Scripts\python.exe"
# Verificar se o ambiente virtual existe
if (Test-Path $venvPath) {
    Write-Host "Ambiente virtual encontrado. Continuando..." -ForegroundColor Green
} else {
    Write-Host "Ambiente virtual não encontrado. Criando..." -ForegroundColor Yellow
    python -m venv venv
}

# Atualizar pip
Write-Host "Atualizando pip..." -ForegroundColor Cyan
& $venvPath -m pip install --upgrade pip

# Instalar flake8
Write-Host "Instalando flake8..." -ForegroundColor Cyan
& $venvPath -m pip install flake8

# Verificar versão do flake8
Write-Host "Verificando instalação do flake8..." -ForegroundColor Cyan
& .\venv\Scripts\flake8.exe --version
Write-Host "Tudo pronto! ✅" -ForegroundColor Green
# Caminho do ambiente virtual[flake8]
exclude = .git, __pycache__, env, venv, .venv, build, dist, migrations
max-line-length = 120

$venvPath = ".\venv\Scripts\python.exe"

# Verificar se o ambiente virtual existe
if (Test-Path $venvPath) {
    Write-Host "Ambiente virtual encontrado. Continuando..." -ForegroundColor Green
} else {
    Write-Host "Ambiente virtual não encontrado. Criando..." -ForegroundColor Yellow
    python -m venv venv
}

# Atualizar pip
Write-Host "Atualizando pip..." -ForegroundColor Cyan
& $venvPath -m pip install --upgrade pip

# Instalar flake8
Write-Host "Instalando flake8..." -ForegroundColor Cyan
& $venvPath -m pip install flake8

# Verificar versão do flake8
Write-Host "Verificando instalação do flake8..." -ForegroundColor Cyan
& .\venv\Scripts\flake8.exe --version

Write-Host "Tudo pronto! ✅" -ForegroundColor Green


Write-Host "Script de correção automática"
# Seu conteúdo do script aqui
<#
.SYNOPSIS
    Script de correção automática para projetos Flask
.DESCRIPTION
    Este script automatiza a configuração do ambiente virtual,
    instalação de dependências e correção de problemas comuns
    em aplicações Flask.
#>

# Configurações
$VENV_DIR = "venv"
$REQUIREMENTS = @("flask", "flask-sqlalchemy", "flask-login", "flask-wtf", "python-dotenv", "flake8")

function Initialize-Environment {
    Write-Host "`n=== VERIFICANDO AMBIENTE ===`n" -ForegroundColor Cyan
    
    # Verifica se o Python está instalado
    try {
        $pythonVersion = python --version
        Write-Host "Python encontrado: $pythonVersion" -ForegroundColor Green
    } catch {
        Write-Host "Python não encontrado. Instale Python primeiro." -ForegroundColor Red
        exit 1
    }

    # Cria/reativa o ambiente virtual
    if (-not (Test-Path $VENV_DIR)) {
        Write-Host "Criando ambiente virtual..." -ForegroundColor Yellow
        python -m venv $VENV_DIR
    }

    Write-Host "Ativando ambiente virtual..." -ForegroundColor Yellow
    .\venv\Scripts\Activate

    # Atualiza pip
    Write-Host "Atualizando pip..." -ForegroundColor Yellow
    python -m pip install --upgrade pip
}

function Install-Dependencies {
    Write-Host "`n=== INSTALANDO DEPENDÊNCIAS ===`n" -ForegroundColor Cyan
    
    foreach ($package in $REQUIREMENTS) {
        Write-Host "Instalando $package..." -ForegroundColor Yellow
        pip install $package
    }
}

function Fix-File-Formatting {
    Write-Host "`n=== CORRIGINDO FORMATAÇÃO ===`n" -ForegroundColor Cyan
    
    Get-ChildItem -Recurse -Filter *.py | ForEach-Object {
        try {
            $content = Get-Content $_.FullName -Raw -ErrorAction Stop
            if ($null -ne $content) {
                $corrected = $content.TrimEnd() + "`n"
                Set-Content $_.FullName $corrected -NoNewline
                Write-Host "Arquivo $($_.Name) formatado" -ForegroundColor Green
            }
        } catch {
            Write-Host "Erro ao processar $($_.Name): $_" -ForegroundColor Red
        }
    }
}

function Run-Flask-App {
    Write-Host "`n=== INICIANDO APLICAÇÃO ===`n" -ForegroundColor Cyan
    
    # Verifica se run.py existe
    if (-not (Test-Path "run.py")) {
        Write-Host "Criando run.py básico..." -ForegroundColor Yellow
        @'
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
'@ | Set-Content run.py -Encoding UTF8
    }

    # Executa a aplicação
    try {
        Write-Host "Iniciando Flask..." -ForegroundColor Green
        python run.py
    } catch {
        Write-Host "Erro ao iniciar a aplicação: $_" -ForegroundColor Red
    }
}

# Execução principal
Initialize-Environment
Install-Dependencies
Fix-File-Formatting
Run-Flask-App
Write-Host "`n=== Limpando projeto Flask: __pycache__ e arquivos .pyc ===`n" -ForegroundColor Cyan

$projectRoot = "C:\Users\clove\Documents\viral_video_app"

Write-Host "Removendo pastas __pycache__..." -ForegroundColor Yellow
Get-ChildItem -Path $projectRoot -Recurse -Directory -Filter "__pycache__" | ForEach-Object {
    Remove-Item $_.FullName -Recurse -Force
    Write-Host "Deletado: $($_.FullName)" -ForegroundColor Green
}

Write-Host "`nRemovendo arquivos .pyc..." -ForegroundColor Yellow
Get-ChildItem -Path $projectRoot -Recurse -Filter "*.pyc" | ForEach-Object {
    Remove-Item $_.FullName -Force
    Write-Host "Deletado: $($_.FullName)" -ForegroundColor Green
}

$duplicateRun = Join-Path $projectRoot "app\run.py"
if (Test-Path $duplicateRun) {
    Write-Host "`nRemovendo run.py duplicado dentro de /app..." -ForegroundColor Yellow
    Remove-Item $duplicateRun -Force
    Write-Host "Deletado: $duplicateRun" -ForegroundColor Green
} else {
    Write-Host "`nNenhum run.py duplicado encontrado dentro de /app." -ForegroundColor Gray
}

Write-Host "`n=== Limpeza concluída! ===" -ForegroundColor Cyan

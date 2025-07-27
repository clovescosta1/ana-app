Get-ChildItem -Recurse -Filter *.py | ForEach-Object {
    try {
        $content = Get-Content $_.FullName -Raw -ErrorAction Stop
        if ($null -ne $content) {
            $corrected = $content.TrimEnd() + "`n"
            Set-Content $_.FullName $corrected -NoNewline
            Write-Host "Arquivo $($_.Name) formatado com sucesso"
        }
        else {
            Set-Content $_.FullName "`n" -NoNewline
            Write-Host "Arquivo vazio $($_.Name) corrigido"
        }
    }
    catch {
        Write-Host "Erro ao processar $($_.Name): $_" -ForegroundColor Red
    }
}

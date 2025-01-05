Write-Host "Running D:\Dropbox\Projects\BEE\SqlDbWrpr\install.ps1..." -ForegroundColor Yellow
if (Test-Path -Path $env:PROJECT_DIR\pyproject.toml)
    {poetry install}

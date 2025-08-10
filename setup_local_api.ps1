# Setup Local ChatGPT API - PowerShell Script
# This script will help you set up the local ChatGPT API from PawanOsman/ChatGPT

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Setting up Local ChatGPT API" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Node.js is installed
Write-Host "Checking Node.js installation..." -ForegroundColor Yellow
try {
    $nodeVersion = node --version
    Write-Host "✅ Node.js found: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Node.js not found!" -ForegroundColor Red
    Write-Host "Please install Node.js v19+ from https://nodejs.org/" -ForegroundColor Red
    Write-Host "After installation, run this script again." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if git is installed
Write-Host "Checking Git installation..." -ForegroundColor Yellow
try {
    $gitVersion = git --version
    Write-Host "✅ Git found: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Git not found!" -ForegroundColor Red
    Write-Host "Please install Git from https://git-scm.com/" -ForegroundColor Red
    Write-Host "After installation, run this script again." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Create local-api directory if it doesn't exist
$localApiDir = "local-api"
if (!(Test-Path $localApiDir)) {
    Write-Host "Creating local-api directory..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Path $localApiDir | Out-Null
}

# Change to local-api directory
Set-Location $localApiDir

# Clone the repository if it doesn't exist
if (!(Test-Path "ChatGPT")) {
    Write-Host "Cloning PawanOsman/ChatGPT repository..." -ForegroundColor Yellow
    git clone https://github.com/PawanOsman/ChatGPT.git
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Failed to clone repository!" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
    Write-Host "✅ Repository cloned successfully!" -ForegroundColor Green
} else {
    Write-Host "✅ Repository already exists, updating..." -ForegroundColor Yellow
    Set-Location "ChatGPT"
    git pull
    Set-Location ".."
}

# Change to ChatGPT directory
Set-Location "ChatGPT"

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Yellow
npm install
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to install dependencies!" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "✅ Dependencies installed successfully!" -ForegroundColor Green

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Setup Complete!" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "To start the local ChatGPT API:" -ForegroundColor Green
Write-Host "1. Open a new terminal/command prompt" -ForegroundColor White
Write-Host "2. Navigate to: $((Get-Location).Path)" -ForegroundColor White
Write-Host "3. Run: npm start" -ForegroundColor White
Write-Host "4. The API will be available at: http://localhost:3040" -ForegroundColor White
Write-Host ""
Write-Host "Then in another terminal, start your Flask app:" -ForegroundColor Green
Write-Host "python app.py" -ForegroundColor White
Write-Host ""
Write-Host "Your ChatGPT Clone will now use the local AI model!" -ForegroundColor Green
Write-Host ""

Read-Host "Press Enter to exit"

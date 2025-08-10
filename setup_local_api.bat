@echo off
echo ========================================
echo    Setting up Local ChatGPT API
echo ========================================
echo.

echo Checking Node.js installation...
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed or not in PATH
    echo Please install Node.js v19+ from https://nodejs.org/
    echo After installation, run this script again.
    pause
    exit /b 1
)

echo Node.js found! Checking Git installation...
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed or not in PATH
    echo Please install Git from https://git-scm.com/
    echo After installation, run this script again.
    pause
    exit /b 1
)

echo Git found! Creating local-api directory...
if not exist "local-api" mkdir local-api
cd local-api

echo Cloning PawanOsman/ChatGPT repository...
if not exist "ChatGPT" (
    git clone https://github.com/PawanOsman/ChatGPT.git
    if errorlevel 1 (
        echo ERROR: Failed to clone repository!
        pause
        exit /b 1
    )
    echo Repository cloned successfully!
) else (
    echo Repository already exists, updating...
    cd ChatGPT
    git pull
    cd ..
)

cd ChatGPT

echo Installing dependencies...
npm install
if errorlevel 1 (
    echo ERROR: Failed to install dependencies!
    pause
    exit /b 1
)

echo.
echo ========================================
echo    Setup Complete!
echo ========================================
echo.
echo To start the local ChatGPT API:
echo 1. Open a new terminal/command prompt
echo 2. Navigate to: %CD%
echo 3. Run: npm start
echo 4. The API will be available at: http://localhost:3040
echo.
echo Then in another terminal, start your Flask app:
echo python app.py
echo.
echo Your ChatGPT Clone will now use the local AI model!
echo.

pause

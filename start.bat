@echo off
echo ========================================
echo    ChatGPT Clone 2.0 - Starting Up
echo ========================================
echo.

echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://python.org
    pause
    exit /b 1
)

echo Python found! Installing dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo Dependencies installed successfully!
echo Starting ChatGPT Clone...
echo.
echo The application will open at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.

python app.py

pause

#!/bin/bash

echo "========================================"
echo "   ChatGPT Clone 2.0 - Starting Up"
echo "========================================"
echo

echo "Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.7+ from https://python.org"
    exit 1
fi

echo "Python found! Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

echo
echo "Dependencies installed successfully!"
echo "Starting ChatGPT Clone..."
echo
echo "The application will open at: http://localhost:5000"
echo "Press Ctrl+C to stop the server"
echo

python3 app.py

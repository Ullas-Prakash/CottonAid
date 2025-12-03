#!/bin/bash

echo "========================================"
echo "Cotton Disease Detection - Dev Setup"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python is not installed"
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "ERROR: Node.js is not installed"
    exit 1
fi

echo "[1/4] Installing Python dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install Python dependencies"
    exit 1
fi

echo ""
echo "[2/4] Installing frontend dependencies..."
cd frontend
npm install
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install frontend dependencies"
    exit 1
fi
cd ..

echo ""
echo "[3/4] Starting Flask backend..."
python3 app_with_api.py &
FLASK_PID=$!
sleep 3

echo ""
echo "[4/4] Starting React frontend..."
cd frontend
npm run dev &
REACT_PID=$!
cd ..

echo ""
echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "Flask Backend:  http://127.0.0.1:5000/"
echo "React Frontend: http://localhost:5173/"
echo "API Health:     http://127.0.0.1:5000/api/health"
echo ""
echo "Press Ctrl+C to stop both servers"
echo ""

# Wait for Ctrl+C
trap "kill $FLASK_PID $REACT_PID; exit" INT
wait

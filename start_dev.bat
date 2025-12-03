@echo off
echo ========================================
echo Cotton Disease Detection - Dev Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed or not in PATH
    pause
    exit /b 1
)

echo [1/4] Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install Python dependencies
    pause
    exit /b 1
)

echo.
echo [2/4] Installing frontend dependencies...
cd frontend
call npm install
if errorlevel 1 (
    echo ERROR: Failed to install frontend dependencies
    pause
    exit /b 1
)
cd ..

echo.
echo [3/4] Starting Flask backend...
start "Flask Backend" cmd /k "python app_with_api.py"
timeout /t 3 /nobreak >nul

echo.
echo [4/4] Starting React frontend...
cd frontend
start "React Frontend" cmd /k "npm run dev"
cd ..

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Flask Backend:  http://127.0.0.1:5000/
echo React Frontend: http://localhost:5173/
echo API Health:     http://127.0.0.1:5000/api/health
echo.
echo Press any key to exit this window...
echo (Backend and Frontend will keep running)
pause >nul

@echo off
REM ════════════════════════════════════════════════════════════════════════════
REM BugBounty Toolkit - Windows One-Click Installer
REM Version: 1.0
REM Author: Nobody
REM ════════════════════════════════════════════════════════════════════════════

setlocal enabledelayedexpansion

REM Color definitions
set "GREEN=[92m"
set "RED=[91m"
set "YELLOW=[93m"
set "BLUE=[94m"
set "RESET=[0m"

echo.
echo ╔════════════════════════════════════════════════════════════════════════╗
echo ║                                                                        ║
echo ║              BugBounty Toolkit - Windows Installer                     ║
echo ║                                                                        ║
echo ║  This script will:                                                     ║
echo ║  1. Check Python installation                                          ║
echo ║  2. Create virtual environment                                         ║
echo ║  3. Install dependencies                                               ║
echo ║  4. Setup the toolkit                                                  ║
echo ║                                                                        ║
echo ╚════════════════════════════════════════════════════════════════════════╝
echo.

REM Check if Python is installed
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo [ERROR] Python is not installed or not in PATH!
    echo.
    echo Please install Python 3.9 or higher from:
    echo   https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)

python --version
echo [OK] Python found!
echo.

REM Check if venv exists
if exist "venv" (
    echo Virtual environment already exists.
    echo Skipping creation...
) else (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] Failed to create virtual environment!
        pause
        exit /b 1
    )
    echo [OK] Virtual environment created!
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Failed to activate virtual environment!
    pause
    exit /b 1
)
echo [OK] Virtual environment activated!
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip --quiet
if errorlevel 1 (
    echo [WARNING] Failed to upgrade pip, continuing anyway...
)
echo [OK] pip upgraded!
echo.

REM Install requirements
echo Installing dependencies from requirements.txt...
if not exist "requirements.txt" (
    echo [ERROR] requirements.txt not found!
    pause
    exit /b 1
)

pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies!
    echo.
    echo Possible solutions:
    echo 1. Check your internet connection
    echo 2. Run as Administrator
    echo 3. Check that requirements.txt is in the correct location
    echo.
    pause
    exit /b 1
)
echo [OK] Dependencies installed!
echo.

REM Run setup script
if exist "Setup.py" (
    echo Running setup script...
    python Setup.py
    if errorlevel 1 (
        echo [WARNING] Setup script encountered an issue.
    )
) else (
    echo [WARNING] Setup.py not found, skipping...
)
echo.

REM Success message
echo ╔════════════════════════════════════════════════════════════════════════╗
echo ║                    INSTALLATION COMPLETED!                             ║
echo ╚════════════════════════════════════════════════════════════════════════╝
echo.
echo Next steps:
echo 1. Double-click "run.bat" to start the toolkit
echo    OR
echo 2. Open Command Prompt in this folder and type:
echo    venv\Scripts\activate.bat
echo    python BugbountyToolkit.py
echo.
pause

@echo off
REM ════════════════════════════════════════════════════════════════════════════
REM BugBounty Toolkit - Windows Launcher
REM Version: 1.0
REM Author: Nobody
REM ════════════════════════════════════════════════════════════════════════════

setlocal enabledelayedexpansion

REM Check if virtual environment exists
if not exist "venv" (
    echo.
    echo [ERROR] Virtual environment not found!
    echo.
    echo Please run install.bat first to set up the toolkit.
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Run the toolkit
echo.
echo ╔════════════════════════════════════════════════════════════════════════╗
echo ║           BugBounty Toolkit - Launching Application                    ║
echo ╚════════════════════════════════════════════════════════════════════════╝
echo.

if not exist "BugbountyToolkit.py" (
    echo [ERROR] BugbountyToolkit.py not found!
    pause
    exit /b 1
)

python BugbountyToolkit.py

REM Keep window open if there's an error
if errorlevel 1 (
    echo.
    echo [ERROR] The toolkit encountered an error!
    pause
)

exit /b 0

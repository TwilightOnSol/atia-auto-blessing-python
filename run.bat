@echo off
REM Atia Shrine Automation - Launcher

setlocal enabledelayedexpansion
color 0C

title Atia's Blessing - Automated

echo.
echo ============================================
echo   Atia's Blessing Automation
echo ============================================
echo.

REM Check if privateKeys exists
if not exist "privateKeys" (
    echo [ERROR] privateKeys file not found!
    echo.
    echo Please run install.bat first to set up the application.
    echo.
    pause
    exit /b 1
)

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo.
    echo Please reinstall Python or check your PATH settings.
    echo.
    pause
    exit /b 1
)

REM Run the application
echo Starting Atia's Blessing automation...
echo Runs daily at 05:05 UTC
echo.
echo Press Ctrl+C to stop the application
echo.

python -m src.main

if errorlevel 1 (
    echo.
    echo [ERROR] Application exited with error
    echo.
    pause
)

exit /b 0

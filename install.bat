@echo off
REM Atia Shrine Automation - Python Installer
REM Windows batch script for easy setup

setlocal enabledelayedexpansion
color 0C

echo.
echo ============================================
echo   Atia's Blessing - Python Installer
echo ============================================
echo.

REM Check if Python is installed
echo Checking for Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo [ERROR] Python is not installed or not in PATH
    echo.
    echo Please install Python 3.10+ from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

REM Get Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [OK] Found Python %PYTHON_VERSION%
echo.

REM Check if pip is installed
echo Checking for pip...
pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip is not installed
    pause
    exit /b 1
)
echo [OK] pip is available
echo.

REM Install dependencies
echo ============================================
echo Installing dependencies...
echo ============================================
echo.
pip install -q -r requirements.txt
if errorlevel 1 (
    echo.
    echo [ERROR] Failed to install dependencies
    echo Please check your internet connection and try again.
    echo.
    pause
    exit /b 1
)
echo [OK] Dependencies installed successfully
echo.

REM Create privateKeys file if it doesn't exist
if not exist "privateKeys" (
    echo ============================================
    echo Setting up configuration...
    echo ============================================
    echo.
    copy privateKeys.example privateKeys >nul
    echo [OK] Created privateKeys file from template
    echo.
    echo [!] IMPORTANT: Edit privateKeys with your wallet private keys
    echo [!] Default keys in the file are examples only
    echo [!] Location: privateKeys
    echo.
) else (
    echo [OK] privateKeys file already exists
    echo.
)

REM Offer to open editor for privateKeys
echo ============================================
echo Configuration
echo ============================================
echo.
echo Would you like to edit the privateKeys file now?
echo Press Y to open with Notepad, or N to skip
echo.
set /p EDIT_CONFIG="Edit privateKeys? (Y/N): "

if /i "%EDIT_CONFIG%"=="Y" (
    notepad privateKeys
    echo.
)

REM Final summary
echo.
echo ============================================
echo   Setup Complete!
echo ============================================
echo.
echo To start the application, run:
echo   python src/main.py
echo.
echo The app will automatically activate blessings
echo at 05:05 UTC every day.
echo.
echo Press any key to exit...
pause >nul
exit /b 0

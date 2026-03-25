@echo off
REM Atia Shrine Automation - Dependency Checker

setlocal enabledelayedexpansion
color 0C

echo.
echo ============================================
echo   Dependency Checker
echo ============================================
echo.

REM Check Python
echo Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [FAIL] Python not found
    set PYTHON_OK=0
) else (
    for /f "tokens=2" %%i in ('python --version 2^>^&1') do (
        echo [OK] Python %%i
    )
    set PYTHON_OK=1
)
echo.

REM Check pip
if %PYTHON_OK%==1 (
    echo Checking pip...
    pip --version >nul 2>&1
    if errorlevel 1 (
        echo [FAIL] pip not found
        set PIP_OK=0
    ) else (
        for /f "tokens=2" %%i in ('pip --version 2^>^&1') do (
            echo [OK] pip %%i
        )
        set PIP_OK=1
    )
    echo.
)

REM Check Python packages
if %PIP_OK%==1 (
    echo Checking required packages...
    
    python -c "import web3" >nul 2>&1
    if errorlevel 1 (
        echo [FAIL] web3 not installed
    ) else (
        echo [OK] web3 installed
    )
    
    python -c "import schedule" >nul 2>&1
    if errorlevel 1 (
        echo [FAIL] schedule not installed
    ) else (
        echo [OK] schedule installed
    )
    
    python -c "import colorama" >nul 2>&1
    if errorlevel 1 (
        echo [FAIL] colorama not installed
    ) else (
        echo [OK] colorama installed
    )
    
    echo.
)

REM Check config file
echo Checking configuration...
if exist "privateKeys" (
    echo [OK] privateKeys file found
) else (
    echo [FAIL] privateKeys file not found
    echo [INFO] Run install.bat to set it up
)
echo.

REM Check project files
echo Checking project files...
if exist "src\main.py" (
    echo [OK] src\main.py found
) else (
    echo [FAIL] src\main.py not found
)

if exist "src\config.py" (
    echo [OK] src\config.py found
) else (
    echo [FAIL] src\config.py not found
)

if exist "src\modules\atia.py" (
    echo [OK] src\modules\atia.py found
) else (
    echo [FAIL] src\modules\atia.py not found
)
echo.

echo ============================================
echo   Check Complete
echo ============================================
echo.
echo If all checks pass, you can run:
echo   run.bat
echo.
pause
exit /b 0

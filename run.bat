@echo off
REM Zip Extractor Pro - Windows Launch Script
REM This script launches the Zip Extractor application

echo.
echo ========================================
echo   Zip Extractor Pro
echo   Starting application...
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python 3.6 or higher from https://www.python.org/
    echo.
    pause
    exit /b 1
)

REM Display Python version
echo Using: 
python --version
echo.

REM Run the application
python ZipExtractor.py

REM Check if the application exited with an error
if %errorlevel% neq 0 (
    echo.
    echo ERROR: Application encountered an error!
    echo.
    pause
)

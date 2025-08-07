@echo off
rem Set code page to UTF-8 to handle special characters in path
chcp 65001

rem Change the current directory to the location of this batch file.
cd /d "%~dp0"

echo ===================================================================
echo DEBUGGING INFO:
echo.
echo Batch file location (should be the project directory):
echo %~dp0
echo.

echo Checking for required files...
echo Python executable path: "%~dp0venv\Scripts\python.exe"
if exist "%~dp0venv\Scripts\python.exe" (
    echo OK: Python executable found.
) else (
    echo ERROR: Python executable NOT found at the path above!
)

echo Waitress script path: "%~dp0run_waitress.py"
if exist "%~dp0run_waitress.py" (
    echo OK: Waitress script found.
) else (
    echo ERROR: Waitress script NOT found at the path above!
)
echo.
echo ===================================================================

echo.
echo Starting server with Waitress...
"%~dp0venv\Scripts\python.exe" "%~dp0run_waitress.py"

pause
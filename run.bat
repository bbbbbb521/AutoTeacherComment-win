@echo off
title AutoTeacherComment
echo ========================================
echo   Teacher Comment Helper - Windows Desktop
echo ========================================
echo.

:: Try specific Python paths first
set FOUND_PYTHON=

for %%p in (
    "%LOCALAPPDATA%\Programs\Python\Python313\python.exe"
    "%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
    "%LOCALAPPDATA%\Programs\Python\Python311\python.exe"
    "%LOCALAPPDATA%\Programs\Python\Python310\python.exe"
    "%ProgramFiles%\Python313\python.exe"
    "%USERPROFILE%\miniconda3\python.exe"
) do (
    if exist %%p (
        set FOUND_PYTHON=%%~p
        goto found
    )
)

:: Fallback: try python from PATH
for /f %%i in ('where python 2^>nul') do (
    set FOUND_PYTHON=%%i
    goto found
)

echo [ERROR] Python not found.
pause
exit /b 1

:found
echo Using: %FOUND_PYTHON%
%FOUND_PYTHON% main.py

if errorlevel 1 (
    echo.
    echo [ERROR] Failed. Try: %FOUND_PYTHON% -m pip install -r requirements.txt
    pause
)
pause

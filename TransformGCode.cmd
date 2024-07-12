@echo off

set PYTHON=U:\Python\3.8\python.exe
set PYTHON_SCRIPT=%~dp0TransformGCode.py

set infile=%~dpnx1
if "%infile%" == "" echo Error: infile fehlt
if "%infile%" == "" goto end
if not exist "%infile%" echo Error: infile (%infile%) nicht gefunden
if not exist "%infile%" goto end
set outfile=%~dpn1_manual%~x1

::echo infile=[%infile%]
::echo outfile=[%outfile%]

if exist "%outfile%" del "%outfile%" >nul

"%PYTHON%" "%PYTHON_SCRIPT%" "%infile%" "%outfile%"

:end
pause

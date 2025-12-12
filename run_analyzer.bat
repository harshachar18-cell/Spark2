@echo off
echo ==========================================
echo Student Marks Analyzer - Quick Launcher
echo ==========================================
echo.
echo Choose which version to run:
echo 1. Pandas Version (No Java Required) - Press 1
echo 2. Spark Version (Requires Java) - Press 2
echo 3. Exit - Press 3
echo.
choice /c 123 /m "Select option"
if errorlevel 3 goto :exit
if errorlevel 2 goto :spark
if errorlevel 1 goto :pandas

:pandas
cls
echo Running Pandas Version (No Java Required)...
echo.
python student_marks_analyzer_pandas.py
pause
goto :menu

:spark
cls
echo Running Spark Version (Requires Java)...
echo.
python student_marks_analyzer.py
pause
goto :menu

:exit
exit /b
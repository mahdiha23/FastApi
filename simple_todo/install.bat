@echo off
REM Install virtualenv if it's not already installed
pip show virtualenv >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Installing virtualenv...
    pip install virtualenv
)

REM Create a virtual environment
echo Creating virtual environment...
python -m virtualenv myenv

REM Activate the virtual environment
echo Activating virtual environment...
call myenv\Scripts\activate

REM Install required packages
echo Installing packages from requirements.txt...
pip install -r requirements.txt

@echo off

cd myenv/Scripts
call activate
cd ../..
python runserver.py
pause
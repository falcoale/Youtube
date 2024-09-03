@echo off
echo Le librerie si stanno installando...

:: Install pytube
pip install pytube

:: Install requests
pip install requests

echo Installazione completata.
echo Premi invio per avviare il programma, oppure esci.

:: Wait for user input
pause >nul

:: Run the main.py script
python main.py

echo Esecuzione completata.
pause
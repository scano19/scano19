@echo off
cd /d "c:\Users\USER\Desktop\misproyectosIA\scano19"
echo Navigated to: %CD%
echo Initializing Git repository...
git init
git add .
git commit -m "Initial commit: Professional Profile Portfolio"
git branch -M main
git remote add origin https://github.com/scano19/scano19.git
echo Git repository initialized.
pause

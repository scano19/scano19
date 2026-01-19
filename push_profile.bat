@echo off
cd /d "c:\Users\USER\Desktop\misproyectosIA\scano19"
echo Navigated to: %CD%

echo Setting remote origin...
git remote add origin https://github.com/scano19/scano19.git || echo Remote probably already exists

echo Ensuring main branch...
git branch -M main

echo Attempting push to GitHub...
git push -u origin main

pause

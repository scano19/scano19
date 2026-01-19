@echo off
cd /d "c:\Users\USER\Desktop\misproyectosIA\scano19"
echo Navigated to: %CD%

echo Staging changes...
git add .

echo Committing...
git commit -m "Update: Professional Profile README content"

echo Pushing to GitHub...
git push -u origin main

echo Done.
pause

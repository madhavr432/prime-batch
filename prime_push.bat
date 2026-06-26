@echo off
cd /d "C:\prime batch"

:: Add only notebooks, ignore checkpoints
git add *.ipynb

:: Commit with timestamp
git commit -m "Notebook update on %date% %time%"

:: Push to GitHub
git push origin main

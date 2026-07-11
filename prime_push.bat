@echo off
cd /d "C:\prime batch"

:: Add notebooks only (checkpoints ignored via .gitignore)
git add -- "*.ipynb"

:: Format date and time safely
for /f "tokens=1-4 delims=/ " %%a in ("%date%") do set datestamp=%%d-%%b-%%c
for /f "tokens=1-2 delims=:." %%a in ("%time%") do set timestamp=%%a%%b

:: Commit only if staged changes exist
git diff --cached --quiet || git commit -m "Notebook update on %datestamp% %timestamp%"

:: Pull remote changes first (rebase to avoid merge commits)
git stash push -m "auto-stash" || echo No unstaged changes
git pull --rebase origin main
git stash pop || echo No stash to apply

:: Push to GitHub
git push origin main

:: Keep window open
pause

@echo off
cd /d "C:\prime batch"
git add .
git commit -m "Auto update Prime Batch on %date% %time%"
git push origin main

@echo off
:: Enable local variable scope and UTF-8 characters if possible
setlocal enabledelayedexpansion
chcp 65001 >nul

echo ===================================================
echo            PRIME BATCH AUTO-UPLOAD TOOL            
echo ===================================================
echo.

:: Navigate to the directory containing the batch script
cd /d "%~dp0"

:: Verify if Git is installed and repo is initialized
git --version >nul 2>&1
if %errorlevel% NEQ 0 (
    echo [ERROR] Git is not installed or not in the PATH.
    echo Please install Git from https://git-scm.com/ and try again.
    goto end
)

if not exist .git (
    echo [ERROR] This directory is not a Git repository.
    echo Please initialize a Git repository using 'git init' first.
    goto end
)

:: Get current branch name
for /f "tokens=*" %%b in ('git rev-parse --abbrev-ref HEAD') do set "branch=%%b"
echo [INFO] Current Git branch: !branch!

:: Fetch latest remote changes
echo [INFO] Fetching latest changes from remote...
git fetch origin !branch!
if %errorlevel% NEQ 0 (
    echo [WARNING] Could not fetch remote changes. Please check your internet connection.
)

:: Check for local changes
git status --porcelain | findstr /R "^" >nul
if %errorlevel% NEQ 0 (
    :: No local changes, but check if we are behind the remote
    git status | findstr /C:"Your branch is behind" >nul
    if !errorlevel! EQU 0 (
        echo [INFO] No local changes, but your branch is behind origin/!branch!. Pulling changes...
        git pull origin !branch!
        if !errorlevel! NEQ 0 (
            echo [ERROR] Pull failed. Please resolve conflicts manually.
        ) else (
            echo [SUCCESS] Repository updated successfully!
        )
    ) else (
        echo [INFO] Everything is up-to-date! No changes to upload.
    )
    goto end
)

:: Show status of files to be committed
echo [INFO] Detected changes:
git status -s
echo.

:: Prompt for commit message
set "commit_msg="
set /p "commit_msg=Enter commit message (or press Enter for auto-generated message): "

:: Remove quotes if entered by user
if defined commit_msg set "commit_msg=!commit_msg:"=!"

:: Generate automatic commit message using PowerShell for regional independence
if "!commit_msg!"=="" (
    for /f "delims=" %%i in ('powershell -Command "Get-Date -Format 'yyyy-MM-dd HH:mm:ss'"') do set "datetime=%%i"
    set "commit_msg=Auto-upload on !datetime!"
)

echo.
echo [INFO] Staging all changes...
git add -A
if %errorlevel% NEQ 0 (
    echo [ERROR] Failed to stage changes.
    goto end
)

echo [INFO] Committing changes with message: "!commit_msg!"
git commit -m "!commit_msg!"
if %errorlevel% NEQ 0 (
    echo [ERROR] Failed to commit changes.
    goto end
)

:: Pull remote changes first to prevent non-fast-forward rejections
echo [INFO] Pulling remote changes to sync...
git pull --rebase origin !branch!
if %errorlevel% NEQ 0 (
    echo.
    echo [ERROR] Pull/Rebase failed! This usually happens if there are conflicts with remote.
    echo Please resolve the conflicts manually or run:
    echo   git rebase --abort
    goto end
)

:: Push to remote
echo [INFO] Uploading (pushing) changes to remote repository...
git push origin !branch!
if %errorlevel% NEQ 0 (
    echo.
    echo [ERROR] Push failed! Please check git_error.log or console output.
    git push origin !branch! 2>git_error.log
) else (
    echo.
    echo [SUCCESS] Project uploaded successfully to Git/GitHub!
    if exist git_error.log del git_error.log
)

:end
echo.
echo Press any key to exit...
pause >nul

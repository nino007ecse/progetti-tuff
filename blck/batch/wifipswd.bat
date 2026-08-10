@echo off
title wifi password viewer
setlocal enabledelayedexpansion

cls
echo this script shows all saved wifi passwords.
echo you must run as administrator.
pause
cls

echo processing...
echo.
echo ssid               password
echo.

for /f "tokens=2 delims=:" %%a in ('netsh wlan show profiles ^| findstr /i ":"') do (
    set "ssid=%%a"
    set "ssid=!ssid:~1!"
    for /f "tokens=2 delims=:" %%b in ('netsh wlan show profile name^="!ssid!" key^=clear ^| findstr /i "key"') do (
        set "password=%%b"
        set "password=!password:~1!"
        echo !ssid!    !password!
    )
)

echo.
echo done.
pause
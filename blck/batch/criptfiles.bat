@echo off
title file crypt / decrypt tool
setlocal enabledelayedexpansion

:menu
cls
echo choose an option :
echo 1 - crypt a file (creates .crypt)
echo 2 - decrypt a file (reads .crypt)
echo 3 - exit
set /p choice="your choice (1-3) : "

if "%choice%"=="1" goto crypt
if "%choice%"=="2" goto decrypt
if "%choice%"=="3" exit
echo invalid choice & pause & goto menu

:crypt
set "mode=crypt"
set "action=crypt"
goto process

:decrypt
set "mode=decrypt"
set "action=decrypt"
goto process

:process
cls
echo %action% a file
echo.
set /p inputfile="drag your file here : "
set "inputfile=%inputfile:"=%"
if not exist "%inputfile%" ( echo file not found & pause & goto menu )

set /p password="enter your secret password : "

if "%mode%"=="crypt" (
    set "outputfile=%inputfile%.crypt"
) else (
    if "%inputfile:~-6%"==".crypt" (
        set "outputfile=%inputfile:~0,-6%"
    ) else (
        set "outputfile=%inputfile%.dec"
    )
)

set /p custom="do you want a custom output name? (y/n) : "
if /i "!custom!"=="y" (
    set /p outputfile="enter output path and name : "
    set "outputfile=!outputfile:"=%!"
)

echo processing...
powershell -Command "& {
    $pass = '%password%';
    $key = [Text.Encoding]::UTF8.GetBytes($pass);
    $bytes = [IO.File]::ReadAllBytes('%inputfile%');
    $out = New-Object byte[] $bytes.Length;
    for ($i=0; $i -lt $bytes.Length; $i++) {
        $out[$i] = $bytes[$i] -bxor $key[$i %% $key.Length];
    }
    [IO.File]::WriteAllBytes('%outputfile%', $out);
    Write-Host 'done!' -ForegroundColor Green;
}"
if %errorlevel% equ 0 (
    echo.
    echo operation completed.
    echo output file : %outputfile%
) else (
    echo error. check your password for forbidden characters.
)
pause
goto menu
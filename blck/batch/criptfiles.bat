@echo off
title xor crypto tool - base version

:menu
cls
echo choose an option :
echo 1 - crypt a file
echo 2 - decrypt a file
echo 3 - exit
set /p choice="your choice (1-3) : "

if "%choice%"=="1" goto crypt
if "%choice%"=="2" goto decrypt
if "%choice%"=="3" exit
echo invalid choice & pause & goto menu

:crypt
set "action=crypt"
set "mode=crypt"
goto process

:decrypt
set "action=decrypt"
set "mode=decrypt"
goto process

:process
cls
echo %action% a file
echo.
set /p inputfile="enter file path (drag and drop) : "
set "inputfile=%inputfile:"=%"

if not exist "%inputfile%" (
    echo file not found
    pause
    goto menu
)

set /p password="enter password : "

if "%mode%"=="crypt" (
    set "outputfile=%inputfile%.crypt"
) else (
    if "%inputfile:~-6%"==".crypt" (
        set "outputfile=%inputfile:~0,-6%"
    ) else (
        set "outputfile=%inputfile%.dec"
    )
)

echo processing...
powershell -Command "$p='%password%'; $k=[Text.Encoding]::UTF8.GetBytes($p); $b=[IO.File]::ReadAllBytes('%inputfile%'); $o=New-Object byte[] $b.Length; for($i=0;$i -lt $b.Length;$i++){ $o[$i]=$b[$i] -bxor $k[$i %% $k.Length]; }; [IO.File]::WriteAllBytes('%outputfile%', $o); Write-Host 'done!'"

if %errorlevel% equ 0 (
    echo operation completed
    echo output file : %outputfile%
) else (
    echo error during operation
)
pause
goto menu
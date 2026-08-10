@echo off
:menu
echo . . . tulip's spoofer . . .
echo 1 : delete discord logs
echo 2 : delete roblox logs
echo 3 : delete minecraft logs
echo 4 : delete all logs
echo 5 : exit

set /p choice=" : "

if %choice%==1 goto discord
if %choice%==2 goto roblox
if %choice%==3 goto minecraft
if %choice%==4 goto all
if %choice%==5 goto exit
goto menu

:discord
echo deleting discord and all clients logs
del /q %appdata%\discord\local storage\leveldb*.log
del /q %appdata%\discord\local storage\leveldb*.ldb
del /q %appdata%\discord\cache*.*
del /q %appdata%\discord\code cache*.*
del /q %appdata%\discord\blob_storage*.*
del /q %appdata%\discordcanary\local storage\leveldb*.log
del /q %appdata%\discordcanary\local storage\leveldb*.ldb
del /q %appdata%\discordcanary\cache*.*
del /q %appdata%\discordcanary\code cache*.*
del /q %appdata%\discordcanary\blob_storage*.*
del /q %appdata%\discordptb\local storage\leveldb*.log
del /q %appdata%\discordptb\local storage\leveldb*.ldb
del /q %appdata%\discordptb\cache*.*
del /q %appdata%\discordptb\code cache*.*
del /q %appdata%\discordptb\blob_storage*.*
del /q %appdata%\betterdiscord*.*
del /q %appdata%\vencord*.*
del /q %appdata%\lightcord*.*
del /q %appdata%\equicord*.*
del /q %localappdata%\discord*.*
echo done
pause
goto menu

:roblox
del /q %localappdata%\roblox\logs*.*
del /q %localappdata%\roblox\localstorage*.*
del /q %temp%\roblox*.*
echo done
pause
goto menu

:minecraft
del /q %appdata%.minecraft\logs*.*
del /q %appdata%.minecraft\crash-reports*.*
del /q %appdata%.minecraft\launcher_logs*.*
echo done
pause
goto menu

:all
call :discord
call :roblox
call :minecraft
echo done
pause
goto menu

:exit
exit
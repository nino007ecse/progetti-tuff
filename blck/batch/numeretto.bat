@echo off
title giochino carino batcherino DELUXE
color 0b
echo ciau questo giuoco e fatto da blck aka blcklarper
echo versione DELUXE con piu robaz
pause
cls

set /a numero=%random% %% 100 + 1
set tentativi=0
set max_tentativi=15

echo ho sceltoz un numero da unoz a dieciz
echo hai %max_tentativi% tentativi (ma sei scarso quindi te ne do di piu)
echo.

:loop 
set /a tentativi+=1
set /a rimasti=%max_tentativi% - %tentativi% + 1

if %tentativi% gtr %max_tentativi% (
    echo.
    echo HAIII PERSOZZZZ! Il numeroz era %numero%
    echo SEI TROPPO SCARSO FRATELLO
    goto fine
)

echo tentativoz %tentativi% di %max_tentativi% (ancora %rimasti% se non sbaglio)
set /p scelta="inserisciz il tuo numeroz: "

:: controlloz se e numerikoz
echo %scelta%|findstr /r "^[0-9][0-9]*$">nul
if errorlevel 1 (
    echo inserisciz solo numeri stupido!
    set /a tentativi-=1
    goto loop
)

:: controlloz se e nel range
if %scelta% lss 1 (
    echo il numeroz deve essere tra 1 e 100 minus
    set /a tentativi-=1
    goto loop
)
if %scelta% gtr 100 (
    echo il numeroz deve essere tra 1 e 100 minus
    set /a tentativi-=1
    goto loop
)

if %scelta% equ %numero% (
    echo.
    echo COMPLIMENTONI HAI INDOVINATO IN %tentativi% TENTATIVI
    echo SEI UN CAMPIONE
    goto fine
)

:: suggerimentoz
set /a diff=%scelta% - %numero%
if %diff% lss 0 set /a diff=-%diff%

if %diff% leq 3 (
    echo SEI VICINISSIMO BRO
) else if %diff% leq 8 (
    echo sei vicinozzo
) else if %diff% leq 15 (
    echo ni, ne caldo ne freddo
) else (
    echo SEI LONTANO COME TUNG TUNG
)

if %scelta% lss %numero% (
    echo il numeroz e piu ALTOZ scemo
) else (
    echo il numeroz e piu BASSOZ
)

echo.
goto loop

:fine
echo.
echo grazie per aver giocato al giochino carino batcherino
echo fatto da blck aka blcklarper
echo.
echo premere un pulsante per uscire (come nella vita reale)
pause
exit
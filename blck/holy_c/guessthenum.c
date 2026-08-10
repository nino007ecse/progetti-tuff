#include "HolyC"
I64 num, guess, tries;
Srand(Time());
num = Rand() % 100 + 1;
tries = 0;
Print("Indovina il numero (1-100):\n");
while (TRUE) {
  Print("Inserisci il tuo tentativo: ");
  guess = GetI64();
  tries++;
  if (guess < num)
    Print("Troppo basso!\n");
  else if (guess > num)
    Print("Troppo alto!\n");
  else {
    Print("Complimenti! Hai indovinato in %d tentativi.\n", tries);
    break;
  }
}
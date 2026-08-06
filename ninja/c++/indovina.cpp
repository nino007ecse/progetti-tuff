#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
    std::srand(std::time(0));

    int NumeroSegreto = std::rand() % 100 +1;
    int tentativo = 0;
    int tentativifatti = 0;
    std::cout << "Indovina il numero tra 1 e 100!\n" << std::endl;

    do {
        std::cout << "Inserisci il numero: ";
        std::cin >> tentativo;
        tentativifatti++;

        if (tentativo < NumeroSegreto) {
            std::cout << "Troppo basso! Riprova.\n" << std::endl;
        } else if (tentativo > NumeroSegreto) {
            std::cout << "Troppo alto! Riprova.\n" << std::endl;
        } else {
            std::cout << "Congratulazioni! Hai indovinato il numero " << NumeroSegreto << " in " << tentativifatti << " tentativi.\n" << std::endl;
        }
    } while (tentativo != NumeroSegreto);
}

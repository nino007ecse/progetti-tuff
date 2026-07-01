// ===IL CODICE CONTIENE DEGLI ERRORI, SE VUOI AIUTARMI A SISTEMARE IL CODICE SCRIVIMI IN DM SU DISCORD: @schedavideo===
// PUOI MODIFICARE IL CODICE MANDANDOMELO SU DISCORD

#include <iostream>
#include <string>

class ContoBancario {
    private:
        std::string numeroConto;
        std::string pin;
        double saldo;

    public:
        numeroConto = nConto;
        pin = p;
        saldo = saldoIniziale;
};

bool verificaPin(std::string pinInserito) {
    return pin == pinInserito;
};

void mostraSaldo() {
    std::cout << "\nIl tuo saldo attuale è di: " << saldo << " Euro\n"
};

void deposita(double importo) {
    if (importo > 0) {
        saldo += importo;
        std::cout << "Deposito effettuato con successo!\n";
    } else {
        std::cout << "Importo non valido!\n";
    }
};

void preleva(double importo) {
    if (importo <= 0) {
        std::cout << "Errore: l'importo deve essere maggiore di 0.\n";
    } else if (importo > saldo) {
        std::cout << "Errore: saldo insufficente! Operazione annullata.\n";
    } else {
        saldo -= importo;
        std::cout << "Prelievo effettuato con successo|\n";
    }
};

int main() {
    ContoBancario mioConto("IT12345", "1234", 500.0);

    std::string pinInserito;
    std::cout << "===BENVENUTO AL BANCOMAT!===\n";
    std::cout << "Inserisci il tuo pin: ";
    std::cin >> pinInserito;

    if (!mioConto.verificaPin(pinInserito)) {
        std::cout << "Pin errato! Accesso non autorizzato!\n";
        return 0;
    }

    int scelta = 0;
    do {
        std::cout << "\n--- MENU BANCOMAT ---\n";
        std::cout << "\n1. Controlla saldo\n";
        std::cout << "\n2. Deposita euro\n";
        std::cout << "\n3. Preleva euro\n";
        std::cout << "\n3. Esci\n";
        std::cout << "\nScegli un'opzione: ";
        std::cin >> scelta;

        switch(scelta) {
            case 1:
                mioConto.mostraSaldo();
                break;
            case 2:
                double importDep;
                std::cout << "Inserisci la cifra da depositare: ";
                std::cin >> importoDep;
                mioConto.deposito(importoDep);
                break;
            case 3:
                double importoPrel;
                std::cout << "Inserisci la cifra da prelevare: ";
                std::cin >> importoPrel;
                mioConto.preleva(importoPrel);
                break;
            case 4:
                std::cout << "Grazie per aver usato il bancomat!\n";
                break;
            default:
                std::cout << "Opzione non valida!\n";
        }
    } while (scelta != 4);

    return 0;
}

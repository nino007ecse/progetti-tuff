#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Contatto {
    private:
        string nome;
        string telefono;

    public:
        Contatto(string n, string t) : nome(n), telefono(t) {}

        void mostraInfo() const {
            cout << "Nome: " << nome << " | Tel: " << telefono << endl;
        }
};

int main() {
    vector<Contatto> rubrica;

    rubrica.push_back(Contatto("Mario Rossi", "+39 367 676 9676"));
    rubrica.push_back(Contatto("Luca Bianchi", "+39 367 676 9676"));
    rubrica.push_back(Contatto("Giulia Verdi", "+39 367 676 9676"));

    cout << "=== LA TUA RUBRICA ===" << endl;

    for (const auto& contatto : rubrica) {
        contatto.mostraInfo();
    }

    return 0;
}
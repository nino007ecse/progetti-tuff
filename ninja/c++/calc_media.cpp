#include <iostream>
using namespace std;

int main() {
    double num1, num2, num3;

    cout << "Inserisci il primo numero: ";
    cin >> num1;

    cout << "Inserisci il secondo numero: ";
    cin >> num2;

    cout << "Inserisci il terzo numero: ";
    cin >> num3;

    double media = (num1 + num2 + num3) / 3.0;

    cout << "\nLa media dei tre numeri è: " << media << endl;
    return 0;
}
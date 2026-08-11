#include <iostream>
#include <vector>

using namespace std;

void stampaGriglia(const vector<vector<char>>& griglia) {
    cout << "\n";
    for (int i = 0; i < 3; i++) {
        cout << " ";
        for (int j = 0; j < 3; j++) {
            cout << griglia[i][j];
            if (j < 2) cout << " | ";
        }
        cout << "\n";
        if (i < 2) cout << "---|---|---\n";
    }
    cout << "\n";
}

char controllaVincitore(const vector<vector<char>>& griglia) {
    for (int i = 0; i < 3; i++) {
        if (griglia[i][0] == griglia[i][1] && griglia[i][1] == griglia[i][2] && griglia[i][0] != ' ') {
            return griglia[i][0];
        }
        if (griglia[0][i] == griglia[1][i] && griglia[1][i] == griglia[2][i] && griglia[0][i] != ' ') {
            return griglia[0][i];
        }
    }
    // Controlla le diagonali
    if (griglia[0][0] == griglia[1][1] && griglia[1][1] == griglia[2][2] && griglia[0][0] != ' ') {
        return griglia[0][0];
    }
    if (griglia[0][2] == griglia[1][1] && griglia[1][1] == griglia[2][0] && griglia[0][2] != ' ') {
        return griglia[0][2];
    }
    return ' ';
}

bool controlloPareggio(const vector<vector<char>>& griglia) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (griglia[i][j] == ' ') return false;
        }
    }
    return true;
}

int main() {
    vector<vector<char>> griglia(3, vector<char>(3, ' '));
    char giocatoreCorrente = 'X';
    char vincitore = ' ';
    int mossaR, mossaC;

    cout << "=== TRIS ===\n";
    while (true) {
        stampaGriglia(griglia);
        cout << "Turno del giocatore " << giocatoreCorrente << ". Inserisci riga e colonna: ";
        cin >> mossaR >> mossaC;
        if (mossaR >= 0 && mossaR < 3 && mossaC >= 0 && mossaC < 3 && griglia[mossaR][mossaC] == ' ') {
            griglia[mossaR][mossaC] = giocatoreCorrente;
            vincitore = controllaVincitore(griglia);
            if (vincitore != ' ') {
                cout << "Il giocatore " << vincitore << " ha vinto!\n";
                break;
            }
            if (controlloPareggio(griglia)) {
                cout << "Pareggio!\n";
                break;
            }
            giocatoreCorrente = (giocatoreCorrente == 'X') ? 'O' : 'X';
        } else {
            cout << "Mossa non valida. Riprova.\n";
        }
    }
    return 0;
}
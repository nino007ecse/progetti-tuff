#include <stdio.h>

int main() {
    int età;

    printf("Inserisci l'età dello studente: ");
    scanf("%d", &età);

    if (età < 0) {
        printf("L'età inserita non è valida\n");
    }

    else if (età >= 18) {
        printf("Lo studente è maggiorenne\n");
    }
    else {
        printf("Lo studente è minorenne\n");
    }

    return 0;
}

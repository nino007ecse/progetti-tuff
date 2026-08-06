def calcolatrice():
    print("=== CALCOLATRICE ===")
    a = float(input("Inserisci il primo numero: "))
    op = input("Inserisci l'operatore (+, -, *, /): ")
    b = float(input("Inserisci il secondo numero: "))

    if op == '+':
        print(f"Risultato: {a + b}")
    elif op == '-':
        print(f"Risultato: {a - b}")
    elif op == '*':
        print(f"Risultato: {a * b}")
    elif op == '/':
        if b != 0:
            print(f"Risultato: {a / b}")
        else:
            print("Errore: Divisione per zero!")
    else:
        print("Errore: Operatore non valido!")

if __name__ == "__main__":
    calcolatrice()
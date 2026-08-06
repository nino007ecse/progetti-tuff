import random

def gioca():
    segreto = random.randint(1, 50)
    tentativi = 0
    print("=== INDOVINA IL NUMERO ===")

    while True:
        scelta = int(input("Indovina il numero tra 1 e 50: "))
        tentativi += 1

        if scelta < segreto:
            print("Troppo basso! Riprova.")
        elif scelta > segreto:
            print("Troppo alto! Riprova.")
        else:
            print(f"Complimenti! Hai indovinato il numero {segreto} in {tentativi} tentativi.")
            break

if __name__ == "__main__":
    gioca()
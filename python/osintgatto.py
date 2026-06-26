import time
import sys

def animazione_caricamento(testo, ripetizioni=3):
    """Crea un effetto di caricamento con i puntini."""
    for _ in range(ripetizioni):
        for i in range(4):
            # Sovrascrive la riga corrente
            sys.stdout.write(f"\r{testo}{'.' * i}".ljust(50))
            sys.stdout.flush()
            time.sleep(0.5)
    print() # Va a capo alla fine

def gatto_premium():
    # ASCII Art del gatto con il quadrato
    ascii_art = """
    Aperta Fonte Intelligenza Gatto Primium
    Creato da NonSonoNinja/accoppare per docsare tutti!
    
       |\---/|    __________________________
       | o_o |   |                          |
        \_^_/    |  Con più di 67 api 🐝     |
        /   \    |__________________________|
       /|   |\\
      |_|___|_|
    """
    print(ascii_art)

    # Input dell'utente
    target = input("su chi vuoi fare osint?: ")

    # Sequenza di finte ricerche
    animazione_caricamento("cercando account")
    animazione_caricamento("facendo chiamate con le api 🐝")

    # Risultato finale
    print(f"\nho trovato 6710469 corrispondenze su {target} !")

if __name__ == "__main__":
    try:
        gatto_premium()
    except KeyboardInterrupt:
        print("\n\nRicerca interrotta.")

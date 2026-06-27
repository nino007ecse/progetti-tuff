# codice fatto da : blck/blck67 
# per qualsiasi cosa scrivermi su ds : lasciato
# per aiutarmi nello script scrivermi su ds
# ------------------------------------------------------------------------
import time
import sys

ROSSI = [
    (80, 0, 0),
    (120, 0, 0),
    (160, 20, 20),
    (200, 40, 40),
    (230, 60, 60),
    (255, 80, 80),
    (255, 50, 50),
    (200, 30, 30),
    (150, 10, 10),
    (100, 5, 5),
]

def stampa_con_effetto_rosso_fisso(testo):
    lines = testo.split('\n')
    for line in lines:
        if line.strip():
            testo_colorato = ""
            for i, char in enumerate(line):
                col = ROSSI[i % len(ROSSI)]
                testo_colorato += f"\033[38;2;{col[0]};{col[1]};{col[2]}m{char}"
            print(testo_colorato + "\033[0m")
        else:
            print()

def tigrerossafiglidiputtana():
    ascii_art = r"""
            TIGRE ROSSA FIGLI DI PUTTANA SIETE FOTTUTI >:) 
                                             __,,,,_
                          _ __..-;''`--/'/ /.',-`-.
                      (`/' ` |  \ \ \\ / / / .-'/`,_
                     /'`\ \   |  \ | \| // // / -.,/_,'-,
                    /<7' ;  \ \  | ; ||/ /| | \/    |`-/,/-.,_,/')
                  /  _.-, `,-\,__|  _-| / \ \/|_/  |    '-/.;.\'
                   `-`  f/ ;      / __/ \__ `/ |__/ |
                       `-'      |  -| =|\_  \  |-' |
                              __/   /_..-' `  ),'  //
                          fL ((__.-'((___..-'' \__.'
                """
    
    stampa_con_effetto_rosso_fisso(ascii_art)
    
    print("\033[38;2;255;80;80m\n\nCHI CAZZO DEVE SUBIRE LA POTENZA DI TIGRE ROSSA?:\033[0m")
    target = input()
    
    print("\033[38;2;255;50;50mOSINTANDO . . .\033[0m")
    time.sleep(1)
    print("\033[38;2;200;40;40mDOXXANDO CON LE NOSTRE 537 API\033[0m")
    time.sleep(1)
    
    print(f"\033[38;2;255;80;80m\nHO DOXXATO {target} SIETE FOTTUTI FIGLI DI PUTTANA\033[0m")
    
    time.sleep(2)
    
    print("\033[38;2;230;60;60m\nORA SEI NEI GUAI . . .\033[0m")
    time.sleep(1)
    print("\033[38;2;255;50;50mMUAhahahahahahahahahahah!\033[0m")
    
    print("\033[38;2;255;80;80m\nVUOI SAPERE COSA TI SUCCEDE? (si/no):\033[0m")
    risposta = input()
    
    if risposta.lower() in ["si", "sì"]:
        print("\033[38;2;255;50;50mTI DOXXO TUTTO! NOME, COGNOME, INDIRIZZO, CODICE FISCALE!\033[0m")
        time.sleep(2)
        print("\033[38;2;230;60;60mSEI FOTTUTO!\033[0m")
    else:
        print("\033[38;2;255;80;80mTANTO LO FACCIO LO STESSO!\033[0m")
        time.sleep(1)
        print("\033[38;2;255;50;50mSEI FOTTUTO COMUNQUE!\033[0m")

if __name__ == "__main__":
    try:
        tigrerossafiglidiputtana()
    except KeyboardInterrupt:
        print("\n\n\033[38;2;255;50;50mmi hai fermato? e adesso ti doxxo muahahahaha\033[0m")
        time.sleep(2)
        print("\033[38;2;230;60;60mSEI FOTTUTO!\033[0m")

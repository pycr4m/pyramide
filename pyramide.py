def main():
    hoehe, breite = get_hoehe_breite()
    pyramide_bauen(hoehe, breite)

def get_hoehe_breite():
    while True:
        try:
            hoehe = int(input(f"Gib die Höhe der Pyramide ein: "))
        except ValueError:
            print("Gibt eine positive Ganzzahl > als 0 ein!")
            continue
        if hoehe > 0:
            break
        else:
            print("Gibt eine positive Ganzzahl > als 0 ein!")
            continue
    while True:
        try:
            breite = int(input(f"Gib die Breite der Pyramide ein: "))
        except ValueError:
            print("Gibt eine positive Ganzzahl > als 0 ein!")
            continue
        if breite > 0:
            break
        else:
            print("Gibt eine positive Ganzzahl > als 0 ein!")
            continue
    return hoehe, breite

def pyramide_bauen(hoehe, breite):
    if hoehe <= breite:
        leerzaehler = hoehe
        if hoehe % 2 == 0:
            if breite//2 < hoehe:
                for i in range(1,(breite//2 + 1)):
                    print((leerzaehler-i) *  " "+ (i) * "**")
                print(f"Die Breite {breite} wurde erreicht.")
            else:
                for i in range(1,(hoehe+1)):
                    print((leerzaehler-i) *  " "+ (i) * "**")
                print(f"Die Höhe {hoehe} wurde erreicht.")
        else:
            for i in range(1,(hoehe+1)):
                print((leerzaehler-i) *  " "+ (i) * "* ")
            print(f"Die Höhe {hoehe} wurde erreicht.")
    else:
        leerzaehler = breite
        if breite % 2 == 0:
            for i in range(1,breite//2+1):
                print((leerzaehler-i) *  " "+ (i) * "**")
            print(f"Die Breite {breite} wurde erreicht.")
        else:
            for i in range(1,breite+1):
                print((leerzaehler-i) *  " "+ (i) * "* ")
            print(f"Die Breite {breite} wurde erreicht.")
main()
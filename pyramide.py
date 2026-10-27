def main():
    hoehe = get_wert("Höhe")
    breite = get_wert("Breite")
    pyramide_bauen(hoehe, breite)

def get_wert(seite):
    while True:
        try:
            seite = int(input(f"Gib die {seite} der Pyramide ein: "))
        except ValueError:
            print("Gibt eine positive Ganzzahl > als 0 ein!")
            continue
        if seite > 0:
            return seite
        print("Gibt eine positive Ganzzahl > als 0 ein!")

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
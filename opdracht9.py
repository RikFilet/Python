# hoe zorg je dat er alleen nummer kunnen worden ingevoerd
while True:
    artikelen = int(input("Voer het artikelnummer in. Voer artikelnummer 0 in om te stoppen.\n:"))
    artikelen = str(artikelen)
    if artikelen == "0":
        print("Programma wordt gesloten")
        break
    elif len(artikelen) <= 4:
        print("Artikel nummer moet langer dan 5 karakters zijn. Start het programma opnieuw op")
        break
    naam_artikel = input("Wat is de naam van het artikel?\n:")
    prijs_artikel = input("Hoe duur is het artikel?\n:")
    print("Het artikelnummer is", artikelen , "de naam van het artikel is", naam_artikel , "en het kost", prijs_artikel , "euro")
    print(" -----------\n volgend artikel\n -----------")





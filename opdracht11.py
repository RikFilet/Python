# De int() functie zorgt ervoor dat alleen cijfers ingevoerd kunnen worden
aantaljaar = int(input("Hoeveel jaar wilt u de opslagruimte huren?\n:"))

basishuur = 835

# kosten voor jaar 1 staan vast, deze worden hier dus alvast laten zien
print("De kosten voor jaar 1 zijn:", basishuur * 12)

jaarnummer = 2  # het jaar nummer begint op 2, omdat jaar 1 niet wordt mee genomen in de loop
# de loop word het aantaljaren dat is ingevoerd -1 uitgevoerd. Dit omdat het 1e jaar er nog geen verhooging is
for jaren in range(aantaljaar - 1):
    nieuwe_huur = basishuur / 100 * 101.75  # de formule om de nieuwe huur te berekenen
    basishuur = nieuwe_huur  # zo wordt de huurprijs steeds up to date gehouden
    basishuur = round(basishuur, 2)  # hier ronden we de huurprijs af zodat het er netjes uitziet
    print("De kosten voor jaar", jaarnummer,"zijn:", basishuur * 12)
    jaarnummer += 1  # dit zorgt ervoor dat het jaarnummer steeds wordt up gedatet

# print("dit is de maandhuur van het laatste jaar:", basishuur)


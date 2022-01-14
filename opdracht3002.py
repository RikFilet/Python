#Opgave 3-002

#Een bedrijf huurt 150 computers. Dit kost 12.000 euro per jaar.
#Na het 2de jaar wordt dit elk jaar 2% duurder.
#Schrijf een programma dat de prijs gedurende 15 jaar uitrekent.

#Geef de kosten op het scherm weer voor elk jaar in de zin:

#De kosten voor de computers bedraagt euro {x} in jaar {y}.

#Waarbij de {x} wordt vervangen door het berekende bedrag en {y} door het jaar waarin de kosten worden berekent.


kostencomuters = 12000
jaar = 2
print("De kosten voor de computers bedraagt 12000 euro in jaar 1.")
for i in range (14):
    kostencomuters = kostencomuters * 1.02
    print("De kosten voor de computers bedraagt", round(kostencomuters, ), "euro in jaar", jaar)
    jaar += 1
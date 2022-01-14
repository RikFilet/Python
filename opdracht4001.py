# Opgave 4-001

# De opdracht is om een functie te schrijven die twee getallen opgeteld.

# Vraag in een programma om een gebruiker om het eerste getal in te voeren.

# Schrijf een functie die:
# - een gebruiker om het tweede getal vraagt;
# - het eerste getal met het tweede getal optelt;
# - het resultaat op het scherm toont.

# In het programma die de functie aanroept wordt het totaal ook op het scherm afgedrukt.

# Plaats de functie in een module.

# Roep de module aan. De twee getallen moeten opgeteld worden.

# Noteer multiline commentaar in je programma.

def optellen():  # dit is de functie
    print("Voer twee getallen in om deze op te tellen.")
    a = int(
        input("Wat is uw eerste getal? \n:"))  # Hier wordt om de nummers gevraagt, alleen een int kan worden opgegeven
    b = int(input("Wat is uw tweede getal \n:"))
    c = a + b  # nummers optellen
    print("De uitkomst is:", c)  # uitkomst printen

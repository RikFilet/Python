Naam = input("Wat is uw naam?")
print("Hallo", Naam, "op welke afdeling werk je?")
Afdeling = input("Sales\nICT\nHRM\n:")
if Afdeling == "Sales":
    print("Welke verantwoording heb je?")
    Verantwoording = input("Marketing\nCustomer Care\n:")
    if Verantwoording == "Marketing":
        print("U koos Marketing, Einde")
    elif Verantwoording == "Customer Care":
        print("U koos Customer Care, Einde")
    else:
        print("Kies de afdeling.")
elif Afdeling == "ICT":
    print("Welke verantwoording heb je?")
    Verantwoording = input("DevOps\nSecurity\n:")
    if Verantwoording == "DevOps":
        print("U koos DevOps, Einde")
    elif Verantwoording == "Security":
        print("U koos Security, Einde")
elif Afdeling == "HRM":
    print("Welke verantwoording heb je?")
    Verantwoording = input("Assistant\nManager\n:")
    if Verantwoording == "Assistant":
        print("U koos Assistant, Einde")
    elif Verantwoording == "Manager":
        print("U koos Manager, Einde")
else:
    print("Afdeling niet gevonden LET OP hoofdletter gevoeligheid.")
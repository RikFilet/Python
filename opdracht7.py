print("Lees het netwerk bericht!")
vraag = input("Is het doel bekend?")

if vraag == "ja":
    print("Filter regels worden toegepast.")
    vraag2 = input("Is het netwerk bericht OK?")
    if vraag2 == "ja":
        print("Bericht wordt doorgestuurd.")
    elif vraag2 == "nee":
        print("Netwerk bericht wordt gelogd.")
elif vraag == "nee":
    print("Bericht wordt gedropt.")

print("Einde")

import random
import string
#string.ascii_lowercase


def genereer():
    def letter(i):
        return ''.join(random.choice(string.ascii_lowercase) for x in range(i))

    print("Artikelnummer:", str(random.randint(1000,9999)) + "-" + letter(3) + "-" + letter(3) + "-" + str(random.randint(1000,9999)))


for a in range(10):
    genereer()


#print(random.choice(string.ascii_lowercase))
#print(string.ascii_lowercase)
#print(letter(3))
# def nieuw_nummer():
#nieuw_nummer()

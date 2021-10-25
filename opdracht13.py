import random
import string

# string.ascii_lowercase
def artikelnummer():
    def letter(i):
        return ''.join(random.choice(string.ascii_lowercase[:6]) for x in range(i))

    print("Artikelnummer:", str(random.randint(1000, 9999)) + "-" + letter(3) + "-" + letter(3) + "-" + str(
        random.randint(1000, 9999)))


for a in range(10):
    artikelnummer()

print(string.ascii_lowercase[:6])
print(string.ascii_lowercase[6:12])
print(string.ascii_lowercase[12:18])
print(string.ascii_lowercase[18:26])


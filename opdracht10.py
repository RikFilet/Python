import random
#a = 0
#
#while a < 100:
#    nummer = random.randint(100,999)
#    nummer2 = random.randint(10,99)
#
#    nummer3 = random.randint(100, 999)
#    nummer4 = random.randint(10, 99)
#
#    nummer5 = random.randint(100, 999)
#    nummer6 = random.randint(10, 99)
#    artikelnummer = (str(nummer) + "-" + str(nummer2))
#    artikelnummer2 = (str(nummer3) + "-" + str(nummer4))
#    artikelnummer3 = (str(nummer5) + "-" + str(nummer6))
#    print("Artikelnummer = ",artikelnummer,",", "Artikelnummer = ",artikelnummer2, ",", "Artikelnummer = ",artikelnummer3)
#
#    a += 1
for i in range(1, 101):
   # print(i)
    print("Artikelnummer", str(random.randint(100,999)) + "-" + str(random.randint(10,99)) + ",", end='')
    print("Artikelnummer", str(random.randint(100,999)) + "-" + str(random.randint(10, 99)) + ",", end='')
    print("Artikelnummer", str(random.randint(100, 999)) + "-" + str(random.randint(10, 99)))

a = 10


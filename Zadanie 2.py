# Zistenie či číslo patrí do intervalu

l = input("Napíš číslo: ")

u = input("Napíš najnižšie číslo z intervalu: ")

k = input("Napíš najvyššie číslo z intervalu: ")

if u > k:

    print("Zlé poradie čísiel")

elif u < l < k:

    print("Číslo je v intervale")

else:

    print("Číslo nie je v intervale")




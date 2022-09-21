# Zisťovanie či je súčet dvoch posledných cifier párny

l=input("Napíš číslo s viac ako jednou cifrou: ")

u=input("Napíš číslo s viac ako jednou cifrou: ")

k=len(l)-1

a=len(u)-1

s=l[k]

v=u[a]

o=int(v+s)

if len(l) < 2 or len(u) <2:

	print("Nesplnenie podmienky")

elif o%2==0:

	print("Súčet posledných dvoch cifier čísel je párny")

else:

	print("Súčet posledných dvoch čísel nie je párny")

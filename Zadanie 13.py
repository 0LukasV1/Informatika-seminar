# Určovanie typu trojuholníka

l = input("Napíš najkratšiu stranu trojuholníka: ")

u = input("Napíš ani najdlhšiu a ani najkratšiu stranu: ")

k = input("Napíš najdlhšiu stranu: ")

l=int(l)

u=int(u)

k=int(k)

if l <= u <= k and (l+u)>k:

	if (l**2+u**2)==k**2:

		print("Trojuholník je pravouhlý")

	elif l==k==u:

		print("Trojuholník je rovnostranný")

	elif l==u or u==k or k==l:

		print("Trojuholník je rovnoramenný")

	else:

		print("Trojuholník je obyčajný")

else:

	print("Trojuholník neexistuje")






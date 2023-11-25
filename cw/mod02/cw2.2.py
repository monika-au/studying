import math
d=int(input("Podaj dzień z miesiąca z zakresu 1-31: "))
m=int(input("Podaj numer miesiąca z zakresu 1-12: "))
y=int(input("Podaj rok: "))
print(d,end='.');print(m,end='.');print(y)

if m<3:
    z=y-1
    c=0
else:
    z=y
    c=2

numer = ((23*m//9) + d + 4 + y + z//4 - z//100 + z//400 - c) % 7
#print(numer) tu też można zrobić int albo math.trank lub floor

#krotka
tydzien = "niedziela", "poniedzialek", "wtorek", "sroda", "czwartek", "piatek", "sobota"
print(tydzien[numer])


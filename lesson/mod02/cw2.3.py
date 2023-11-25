import math
d=13
y=int(input("Podaj rok: "))

i=0
month = range(1,13,1)
for m in month:
    if m < 3:
        z = y - 1
        c = 0
    else:
        z = y
        c = 2
    number = ((23*m//9) + d + 4 + y + z//4 - z//100 + z//400 - c) % 7
    #print(number)
    if number == 5: i=i+1

print(f"W roku {y} piątek trzynastego występuje {i}-krotnie")
#wyliczyc ile mamy piatkow 13 w danym roku

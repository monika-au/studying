#import math

x=y=0

while True:
    polecenie=input("podaj rozkaz dla robota:")
    if polecenie =='':
    #if not polecenie:
        break

    kierunek, liczba_krokow = polecenie.split()
    liczba_krokow = int(liczba_krokow)

    match kierunek:
        case 'N': y += liczba_krokow
        case 'S': y -= liczba_krokow
        case 'E': x += liczba_krokow
        case 'W': x -= liczba_krokow
        case other: continue

    print(f"Aktualnie robot znajduje się w położeniu ({x}, {y})")

odleglosc = round((x ** 2 + y ** 2)**0.5,2)
#odleglosc = round(math.sqrt(x ** 2 + y ** 2),2)
#odleglosc = math.hypot(x,y)

print("Robot oddalił się o odległość:",odleglosc)

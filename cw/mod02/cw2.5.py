x = y = 0

while True:
    step = input("Podaj kierunek i o ile kroków przesunie się robot [<kierunek><spacja><liczba kroków>]: ")



    if step[0]=="N":
        y=y+int(step[2:])

    if step[0]=="E":
        x=x+int(step[2:])

    if step[0]=="S":
        y=y-int(step[2:])

    if step[0] == "W":
        x = x - int(step[2:])


    if x>0: print(f"Położenie robota to {x} na wschód,", end=" ")
    elif x==0: print("Położenie robota to punkt startowy dla kierunków wschód-zachód", end=' ')
    else: print(f"Położenie robota to {-x} na zachód,", end=" ")

    if y>0: print(f"oraz {y} na północ")
    elif y==0: print("oraz punkt startowy dla kierunków północ-południe")
    else: print(f"oraz {-y} na południe")
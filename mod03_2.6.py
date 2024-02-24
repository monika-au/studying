#that exercise is made in polish language

liczba = int(input("Podaj liczbę w zakresie 0-999 "))
if liczba<0 or liczba>999:
    print("Liczba spoza zakresu")
    exit()

jednosc = liczba % 10
dziesiatka = int((liczba % 100 - jednosc)/10)
setka = int((liczba - dziesiatka*10 - jednosc) / 100)

jedn = ("","jeden","dwa","trzy","cztery","pięć","sześć","siedem","osiem","dziewięć")
dzi = ("","naście","dwadzieścia","trzydzieści","czterdzieści","pięćdziesiąt","sześćdziesiąt","siedemdziesiąt","osiemdziesiąt","dziewięćdziesiąt")
st = ("","sto","dwieście","trzysta","czterysta","pięćset","sześćset","siedemset","osiemset","dziewięćset")

j = jedn[jednosc]
d = dzi[dziesiatka]
s = st[setka]

slownie = []
if (dziesiatka==1):
    if(jednosc == 1):
        j="jede"
    slownie.append(s)
    slownie.append(j)
    slownie.append(d)
else:
    slownie.append(s)
    slownie.append(d)
    slownie.append(j)

txt=''
for el in slownie:
    txt += el+' '
    

print(txt)
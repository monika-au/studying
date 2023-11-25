data1 = "19/11/2023"
data2 = "19.11.2023"
data3 = "19_11_2023"
# realizacja algorytmu

def rozdziel_date(data,separator):
    rozdzielona_data = data.split(separator)
    dzien, miesiac, rok = rozdzielona_data
    dzien = int(dzien)
    miesiac = int(miesiac)
    rok = int(rok)
    if int(miesiac) < 3:
        z = rok - 1
        c = 0
    else:
        z = rok
        c = 2
    numer_dnia_tygodnia = (23 * miesiac // 9 + dzien + 4 + rok + z // 4 - z // 100 + z // 400 - c) % 7
    print(numer_dnia_tygodnia)
    return numer_dnia_tygodnia

def nazwa_dnia_tygodnia(numer_dnia_tygodnia):
    tydzien = 'niedziela', 'poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota'
    print('Dzien tygodnia to', tydzien[numer_dnia_tygodnia])

numer_dnia = rozdziel_date(data1, "/")
nazwa_dnia_tygodnia(numer_dnia)

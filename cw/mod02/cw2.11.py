import statistics
# Dane wejściowe
osoba1 = {
    'imie': 'Jan',
    'nazwisko': 'Kowalski',
    'adres': 'Poznań',
    'plec': True,
    'wiek': 22
}
osoba2 = {
    'imie': 'Anna',
    'nazwisko': 'Jabłońska',
    'adres': 'Szczecin',
    'plec': False,
    'wiek': 18
}
osoba3 = {
    'imie': 'Tomasz',
    'nazwisko': 'Nowak',
    'adres': 'Wrocław',
    'plec': True,
    'wiek': 30
}
osoba4 = {
    'imie': 'Alicja',
    'nazwisko': 'Młynarska',
    'adres': 'Poznań',
    'plec': False,
    'wiek': 25
}

baza_osob = [osoba1,osoba2,osoba3,osoba4]

panie_a = [osoba['wiek'] for osoba in baza_osob if not osoba['plec'] and osoba['imie'][0] == 'A']
print(panie_a)
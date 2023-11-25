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

print("Mężczyźni z Poznania:")
def predykat_mezczyzn_z_poznania(osoba):
    return osoba['plec'] and osoba['adres']=="Poznań"

mezczyzni_z_poznania = filter(predykat_mezczyzn_z_poznania, baza_osob)
print(*mezczyzni_z_poznania, sep='\n')

print("20-latkowie:")
def predykat_dwudziestolatka(osoba):
    return 20 <= osoba['wiek'] <30

dwudziestolatek = filter(predykat_dwudziestolatka, baza_osob)
print(*dwudziestolatek, sep='\n')


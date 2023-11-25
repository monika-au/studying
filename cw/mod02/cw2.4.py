# losowanie liczb lotto
# wczytanie danych wejściowych
k = int(input('Ile liczb będziesz losował? '))
n = int(input('Spośród ilu liczb? '))

# wyliczenie liczby kombinacji:

# k! silnia
wynik1 = 1
for i in range(1, k+1):
    wynik1 *= i
#   (n − k + 1) ∗ (n − k + 2) ∗ . . . ∗ n
wynik2 = 1
for i in range(n-k+1, n+1):
    wynik2 *= i

liczba_kombinacji = wynik2 // wynik1
# wypisanie wyniku
print('Szansa na trafienie', k, 'liczb z', n, 'wynosi 1 do', liczba_kombinacji)
value = int(input("Podaj liczbę w zakresie od 1 do 3999: "))

if value <1 or value > 3999:
    print("Liczba spoza zakresu")
else:
    arabic = 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
    roman = "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"

    change_to_roman = dict(zip(arabic, roman))
    rzymska=''
    for arabska in arabic:
        while value >= arabska:
            rzymska += change_to_roman[arabska]
            value -= arabska
        if value == 0:
            break
    print(rzymska)

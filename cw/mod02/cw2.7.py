text = "Co mi dał duch? Cud, ład i moc."
text = text.lower()
text = text.replace(",","")
text = text.replace("?","")
text = text.replace(" ","")
list_text = list(text)

print(list_text)

new_text =  text[::-1]

if text == new_text:
    print("Tekst to palindrom")
else:
    print("Tekst nie jest palindromem")


#inny sposób
palindrom_list = [character.lower() for character in text if character.isalpha()]

if palindrom_list == palindrom_list[::-1]:
    print('Podany tekst jest palindromem')
else:
    print('Podany tekst nie jest palindromem')

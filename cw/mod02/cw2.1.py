name = "United Nations Educational, Scientific and Cultural Organization"
shortcut = "" #pusty tekst
splitted = name.split(sep=" ")

for word in splitted:
    fl = '{:.1}'.format(word)
    if fl.isupper():
        print(fl)
        shortcut = shortcut + fl
print(shortcut)


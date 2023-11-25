name = "United Nations Educational, Scientific and Cultural Organization"
shortcut = "" #pusty tekst
splitted = name.split(sep=" ")

print(splitted)

list = "".join(['{:.1}'.format(word) for word in splitted if word[0].isupper()])
print(list)

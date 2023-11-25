year = ("january", "february", "march", "april", "may", "june",
        'july', "august", "september", "october", "november", "december")

quarter = [month for number, month in enumerate(year) if number % 3 == 0]
print(quarter)

#for ele in enumerate(year):
#    print (ele)
year = ("january", "february", "march", "april", "may", "june",
        'july', "august", "september", "october", "november", "december")

month_num = len(year)
quarter_num = 4
quarter_len = month_num//quarter_num

quarter = [[year[nbr_month] for nbr_month in range(month_num) if nbr_month//quarter_len==nbr_quarter] for nbr_quarter in range(quarter_num)]
#do listy przekazuje 4 argumenty
print(*quarter, sep="\n")


import statistics
params_list = []

#information from website https://www.gios.gov.pl/pl/
#chosen Radom , ul. Tochtermana 1
#id - parameter key
keys = ["id", "values"]
keys_values = ["date", "value"]

measure1 = dict(zip(keys, ["PM10",
                       dict(zip(keys_values, ["22.02.2024, 01:00", 24.2]))]))
measure2 = dict(zip(keys, ["PM10",
                       dict(zip(keys_values, ["22.02.2024, 02:00", 22.8]))]))
measure3 = dict(zip(keys, ["PM10",
                       dict(zip(keys_values, ["22.02.2024, 03:00", 23.5]))]))
measure4 = dict(zip(keys, ["PM10",
                       dict(zip(keys_values, ["22.02.2024, 04:00", 22.6]))]))
measure5 = dict(zip(keys, ["PM10",
                       dict(zip(keys_values, ["22.02.2024, 05:00", 21.1]))]))
measure6 = dict(zip(keys, ["PM10",
                       dict(zip(keys_values, ["22.02.2024, 06:00", 17.3]))]))


params_list.append(measure1)
params_list.append(measure2)
params_list.append(measure3)
params_list.append(measure4)
params_list.append(measure5)
params_list.append(measure6)
print(params_list)

#sorting the list by values of parameter from smallest to biggest
sort = sorted(params_list,key=lambda params_list: params_list["values"]["value"])

print("Smallest value of PM10 was", sort[0]["values"]["value"] ,"at", sort[0]["values"]["date"])
print("Biggest value of PM10 was", sort[-1]["values"]["value"] ,"at", sort[-1]["values"]["date"])

z=0
i=0
for val in sort:
    z=z + val["values"]["value"]
    i+=1
print("Mean value of PM10 that day was", z/i)

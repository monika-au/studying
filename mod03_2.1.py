stations_list = []

#information from website https://www.gios.gov.pl/pl/
keys = ["id", "stationName", "gegrLat", "gegrLon", "city", "addressStreet"]
keys_city = ["id", "name", "commune"]
keys_commune = ["communeName", "districtName", "provinceName"]

station1 = dict(zip(keys, [294, "SlZywieKoper", 49.671602, 19.234446,
                       dict(zip(keys_city, [846, "Zywiec", dict(zip(keys_commune, ["Zywiec", "Zywiecki", "Slaskie"]))])),
                       "ul. Kopernika 83 a"]))
station2 = dict(zip(keys, [694, "MpOswiecBema", 50.033083, 19.234446,
                       dict(zip(keys_city, [423, "Oswiecim", dict(zip(keys_commune, ["Oswiecim", "Oswiecimski", "Malopolskie"]))])),
                       "ul. J. Bema"]))
station3 = dict(zip(keys, [809, "MpWadowiBalyMOB", 49.872364, 19.497467,
                       dict(zip(keys_city, [789, "Wadowice", dict(zip(keys_commune, ["Wadowice", "Wadowicki", "Malopolskie"]))])),
                       "ul. Balysa"]))

stations_list.append(station1)
stations_list.append(station2)
stations_list.append(station3)

print(len(stations_list))

for station in stations_list:
    if(station["id"]==294): print("Station with id 294 is",station["stationName"])
    if(station["city"]["name"]=="Wadowice"): print("Station's name from Wadowice is",station["stationName"])
    if(station["city"]["commune"]["provinceName"]=="Malopolskie"): print("Station from Malopolskie is",station["stationName"])
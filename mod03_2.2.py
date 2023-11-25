params_list = []

#information from website https://www.gios.gov.pl/pl/
keys = ["id", "stationId", "param"]
keys_param = ["paramName", "paramFormula", "paramCode", "idParam"]

param1 = dict(zip(keys, [294, 765685,
                       dict(zip(keys_param, ["Carbon monoxide", "CO", "CO",678]))]))
param2 = dict(zip(keys, [355, 48920,
                       dict(zip(keys_param, ["Carbon monoxide", "CO", "CO",678]))]))
param3 = dict(zip(keys, [294, 765685,
                       dict(zip(keys_param, ["Nitrogen Dioxide", "NO2", "NO2",765]))]))
param4 = dict(zip(keys, [432, 65474,
                       dict(zip(keys_param, ["PM10", "PM10", "PM10",547]))]))

params_list.append(param1)
params_list.append(param2)
params_list.append(param3)
params_list.append(param4)

print(len(params_list))

for param in params_list:
    if(param["id"]==294): print("Station with id 294 measures",param["param"]["paramName"])
    if(param["param"]["paramName"]=="Carbon monoxide"): print("Station that measures Carbon monoxide is",param["id"])
    if(param["param"]["paramCode"]=="PM10"): print("ID number for PM10 is",param["param"]["idParam"])
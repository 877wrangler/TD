import json
#read file
myjsonfile = open('data/MJ.json', 'r')
jsondata = myjsonfile.read()

#parse
obj = json.loads(jsondata)

print(str(obj['symbol']))

list1 = (obj['callExpDateMap'])
print(list1)
print(len(list1))
date = list1.get('2021-11-19:5')
print(list1.get('2021-11-19:5'))
print(date.get('15.5'))
strike = date.get('15.5')
print(strike)

word = json[callExpDateMap]

#strike = list.date.get('15.5')
#print(strike.get('mark'))
with open('output.txt', 'w') as f:
    f.write(str((strike)))

#for i in range(len(list)):
#    print("Is", list[i].get('mark'))
import json
#read file
myjsonfile = open('data/MJ.json', 'r')
jsondata = myjsonfile.read()

#parse
obj = json.loads(jsondata)

map = obj['callExpDateMap']
markk = obj['callExpDateMap']['2021-11-19:5']['15.5'][0]['mark']
print(markk)

for mark in map:
   print(mark)


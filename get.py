import requests
import json

url = 'http://papalote.cocoplan.mx/visitante'
data = {'email':'skatvlad@hotail.com'}

r = requests.get(url,data)
print r
tojson = r.json()

print tojson
x = json.dumps(tojson)


print 

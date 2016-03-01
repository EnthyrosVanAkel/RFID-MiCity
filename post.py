import requests



def sumar_puntos(rfid,puntos):
    url = 'http://papalote.cocoplan.mx/v0/agregar_puntos'
    data = {'rfid':rfid,'puntos':puntos}
    r = requests.post(url,data)
    print r



sumar_puntos('1234567890','10')

sumar_puntos('873478243','10')
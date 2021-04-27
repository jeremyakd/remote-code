# numeros = range(11)

#print("Numeros vale: ", numeros)

#print("numeros es de tipo: ", type(numeros))

###################################################

# numeros = list(numeros)

#for i in range(len(numeros)):
#    print(i)

# for numero in numeros:
#     if numero == 0:
#         print("Es cero !!!")
#     elif numero % 2 == 0:
#         print("el numero ", numero, 'es par')
#     else:
#         print("el numero ", numero, 'es "impar"')

x = 0

#while x <= 5:
#    print(x)
#    x += 1
#    if x == 2:
#        print("x vale 2")
#        continue


import requests
import json
import pprint

payload = {
    "token": "81RkYCqb6BRVg7ktJTGDBA",
    "data": {
        "name": "nameFirst",
        "email": "internetEmail",
        "phone": "phoneHome",
        "_repeat": 300
    }
}

r = requests.post("https://app.fakejson.com/q", json = payload)

pprint.pprint(r.json())
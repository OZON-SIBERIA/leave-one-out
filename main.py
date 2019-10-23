import math
import json


def distance(x1, x2, y1, y2, z1, z2, w1, w2):
    return math.sqrt(math.pow((x2-x1), 2)+math.pow((y2-y1), 2)+math.pow((z2-z1), 2)+math.pow((w2-w1), 2))


reading = open("data.json", "r")
jsonstring = reading.read()
reading.close()
data = json.loads(jsonstring)

keys = data.keys()
dictMain = {}
for i in keys:
    keyA = str(i)
    stringA = data[keyA]
    dictAB = {}
    listAB = []
    for key in keys:
        if key != i:
            keyB = str(key)
            stringB = data[keyB]
            classB = stringB["class"]
            f1A = float(stringA["f1"].replace(',', '.'))
            f1B = float(stringB["f1"].replace(',', '.'))
            f2A = float(stringA["f2"].replace(',', '.'))
            f2B = float(stringB["f2"].replace(',', '.'))
            f3A = float(stringA["f3"].replace(',', '.'))
            f3B = float(stringB["f3"].replace(',', '.'))
            f4A = float(stringA["f4"].replace(',', '.'))
            f4B = float(stringB["f4"].replace(',', '.'))
            distanceAB = distance(f1A, f1B, f2A, f2B, f3A, f3B, f4A, f4B)
            listAB.append(distanceAB)
            dictAB[distanceAB] = classB
    print(dictAB)
    dictMain[i] = dictAB
print(dictMain)

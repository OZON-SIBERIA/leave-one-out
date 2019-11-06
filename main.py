import math
import json


def distance(x1, x2, y1, y2, z1, z2, w1, w2):
    return math.sqrt(math.pow((x2-x1), 2)+math.pow((y2-y1), 2)+math.pow((z2-z1), 2)+math.pow((w2-w1), 2))


def jsontopython():
    reading = open("data.json", "r")
    jsonstring = reading.read()
    reading.close()
    data = json.loads(jsonstring)
    return data


data = jsontopython()
keys = data.keys()
dictmain = {}
dictmap = {}
for i in keys:
    keya = str(i)
    stringa = data[keya]
    dictab = {}
    listab = []
    for key in keys:
        if key != i:
            keyb = str(key)
            stringb = data[keyb]
            classb = stringb["class"]
            f1a = float(stringa["f1"].replace(',', '.'))
            f1b = float(stringb["f1"].replace(',', '.'))
            f2a = float(stringa["f2"].replace(',', '.'))
            f2b = float(stringb["f2"].replace(',', '.'))
            f3a = float(stringa["f3"].replace(',', '.'))
            f3b = float(stringb["f3"].replace(',', '.'))
            f4a = float(stringa["f4"].replace(',', '.'))
            f4b = float(stringb["f4"].replace(',', '.'))
            distanceab = distance(f1a, f1b, f2a, f2b, f3a, f3b, f4a, f4b)
            listab.append(distanceab)
            dictab[distanceab] = classb
    print(type(dictab))
    listab = sorted(listab)
    dictmap[i] = listab
    dictmain[i] = dictab


k = 30
for c in enumerate(k):


"""y1 = errorfunction()
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, aspect=1)
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.plot(x, y1, c=(0.25, 0.25, 1.00), lw=2, label="Blue signal", zorder=10)
ax.set_xlabel("X axis label")
ax.set_ylabel("Y axis label")
plt.show()"""

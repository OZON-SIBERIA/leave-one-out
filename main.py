import math

pointA = "01"
pointB = "05"


def distance(x1, x2, y1, y2, z1, z2, w1, w2):
    return math.sqrt(math.pow((x2-x1), 2)+math.pow((y2-y1), 2)+math.pow((z2-z1), 2)+math.pow((w2-w1), 2))


result = distance(5.1, 6.4, 3.5, 3.2, 1.4, 4.5, 0.2, 1.5)
print("distance between", pointA, "and", pointB, ":", result)

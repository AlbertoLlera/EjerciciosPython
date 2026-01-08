import math

def distancia(p1, p2):
    (x1,y1) = p1
    (x2,y2) = p2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

coordenadasTorreEiffiel = (2.2945, 48.8584)
coordenadasEstatuaLibertad = (-74.0445, 40.6892)
print(distancia(coordenadasTorreEiffiel, coordenadasEstatuaLibertad))
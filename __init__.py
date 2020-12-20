import time
from math import log


class Body:
    print('/'*20, time.strftime("%d/%m/%y"), '/'*20)
    print("genere, neck, height, weight, waist, hip")
    print('m 42 171 80 88 0')
    datos = input()
    genere = datos[:1]
    neck, height, weight, waist, hip = map(int, datos[2:].split(" "))

    if genere == 'm':
        fat = 495/(1.0324 - 0.19077 * log((waist-neck), 10) + 0.15456 * log(height, 10)) - 450
        fat_100 = -3.3333 * fat + 126.67
    else:
        fat = 495 / (1.29579 - 0.35004 * log((waist + hip - neck), 10) + 0.22100 * log(height, 10)) - 450
        fat_100 = -2.6316 * fat + 139.49

    lean_mass = (weight * (1 - (fat / 100)))
    ffmi = lean_mass / ((height/100) * (height/100))
    ffmi = ffmi + (6.1 * (1.8 - height/100))
    ffmi_100 = 10* ffmi - 150 if genere == 'm' else 10 * ffmi - 100
    
    index_100 = (fat_100 + ffmi_100) / 2

if __name__ == '__main__':
    body = Body()
    print("Body Fat %: " + str(body.fat))
    print("FFMI: " + str(body.ffmi))
    print('/'*20, 'PUNTAJE / 100', '/'*20)
    print("Fat: " + str(int(body.fat_100)))
    print("Muscle: " + str(int(body.ffmi_100)))
    print("Total: " + str(int(body.index_100)))

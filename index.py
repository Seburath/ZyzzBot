import math
import time
from save_excel import save

while True:
    print("//////////////////////////////", time.strftime("%d/%m/%y"), "///////////////////////////////////")
    print("(genero, estatura, peso, cuello, cintura, cadera)")
    datos = input()

    genere = datos.split(" ")[0]
    height = float(datos.split(" ")[1])
    weight = float(datos.split(" ")[2])
    neck = float(datos.split(" ")[3])
    waist = float(datos.split(" ")[4])
    hip = float(datos.split(" ")[5])

    print("(genero, estatura, peso, cuello, cintura, cadera)")
    print( "   ", genere, "    ", height, " ",weight," ", neck, "  ",waist, "   ",hip)

    if genere is 'm':
    #calculate basic data
        body_fat = 495/(1.0324 - 0.19077 * math.log((waist-neck), 10) + 0.15456 * math.log(height, 10)) - 450
        fat_mass = (body_fat/100) * weight
        lean_mass = (weight * (1 - (body_fat / 100)))
        ffmi = lean_mass / ((height/100) * (height/100))
        ffmi = ffmi + (6.1 * (1.8 - height/100))

    #normalizate It an scale from 0 to 100
        body_fat_100 = -3.3333 * body_fat + 126.67
        ffmi_100 = 10* ffmi - 150
        index_100 = (body_fat_100 + ffmi_100)/2

    if genere is 'f':
        # calculate basic data
        body_fat = 495 / (1.29579 - 0.35004 * math.log((waist + hip - neck), 10) + 0.22100 * math.log(height, 10)) - 450
        fat_mass = (body_fat/100) * weight
        lean_mass = (weight * (1 - (body_fat / 100)))
        ffmi = lean_mass / ((height/100) * (height/100))
        ffmi = ffmi + (6.1 * (1.8 - height/100))

        # normalizate It an scale from 0 to 100
        body_fat_100 = -2.6316 * body_fat + 139.49
        ffmi_100 = 10 * ffmi - 100
        index_100 = (body_fat_100 + ffmi_100) / 2

    print("Grasa Corporal: " + str(body_fat))
    print("Indice de Masa Libre de Grasa: " + str(ffmi))
    print("/////////////////////////// PUNTAJE /100 //////////////////////////////////")
    print("Grasa Corporal: " + str(int(body_fat_100)))
    print("Musculatura: " + str(int(ffmi_100)))
    print("Total: " + str(int(index_100)))
    save(genere, height, weight, neck, waist, hip, body_fat, ffmi, body_fat_100, ffmi_100, index_100)

from openpyxl import load_workbook


def save(genere, height, weight, neck, waist, hip, body_fat, ffmi, body_fat_100, ffmi_100, index_100):
    data = load_workbook(filename = 'data.xlsx')
    sheet = data["Hoja1"]

    def read(hoja, col, row):
        return hoja.cell(column=col, row=row).value

    def write(hoja, col, row, val):
        sheet.cell(column=col, row=row).value = val
        return

    y = hoja.max_row + 1

    write(hoja, 1, y, genere)
    write(hoja, 2, y, height)
    write(hoja, 3, y, weight)
    write(hoja, 4, y, neck)
    write(hoja, 5, y, waist)
    write(hoja, 6, y, hip)
    write(hoja, 7, y, str(body_fat))
    write(hoja, 8, y, str(ffmi))
    write(hoja, 9, y, str(int(body_fat_100)))
    write(hoja, 10, y, str(int(ffmi_100)))
    write(hoja, 11, y, str(int(index_100)))

    print('registro numero: ' + str(hoja.max_row) + ' añadido')
    data.save('data.xlsx')

    return

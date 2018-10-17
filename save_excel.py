from openpyxl import load_workbook

def save(genere, height, weight, neck, waist, hip, body_fat, ffmi, body_fat_100, ffmi_100, index_100):
    data = load_workbook(filename = 'data.xlsx')
    hoja = data["Hoja1"]

    #acotacion dela funcion para obtener valores de excel
    def cell(hoja, col, row):
        return hoja.cell(column=col, row=row).value

    def w_cell(hoja, col, row, val):
        hoja.cell(column=col, row=row).value = val
        return

    y = hoja.max_row + 1

    w_cell(hoja, 1, y, genere)
    w_cell(hoja, 2, y, height)
    w_cell(hoja, 3, y, weight)
    w_cell(hoja, 4, y, neck)
    w_cell(hoja, 5, y, waist)
    w_cell(hoja, 6, y, hip)
    w_cell(hoja, 7, y, str(body_fat))
    w_cell(hoja, 8, y, str(ffmi))
    w_cell(hoja, 9, y, str(int(body_fat_100)))
    w_cell(hoja, 10, y, str(int(ffmi_100)))
    w_cell(hoja, 11, y, str(int(index_100)))

    print('registro numero: ' + str(hoja.max_row) + ' añadido')
    data.save('data.xlsx')

    return

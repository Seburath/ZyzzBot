from openpyxl import load_workbook

def save_excel.save(genere, height, weight, neck, waist, hip, str(body_fat), str(ffmi), str(int(body_fat_100)), str(int(ffmi_100))), str(int(index_100)))):
    return

data = load_workbook(filename = 'data.xlsx')
hoja = data["Hoja1"]

#acotacion dela funcion para obtener valores de excel
def cell(hoja, col, row):
    return hoja.cell(column=col, row=row).value

def w_cell(hoja, col, row, val):
    hoja.cell(column=col, row=row).value = val
    return

#carga valores de /aplicaciones
y=1
for aplicacion in aplicaciones:
    print('Abriendo: ' + aplicacion)
    libro_fuente = load_workbook(filename = 'aplicaciones/' + aplicacion)
    hoja = libro_fuente["Hoja1"]


    if cell(hoja, 11, 1) == 'SGGW-C001': #si el codigo no es 'SGGW-C001' se ignora registro
        print(colored('codigo:SGGW-C001', 'yellow', 'on_grey'))
        ap = collections.OrderedDict()
        ap = {  'form_num': cell(hoja, 2, 8),
                'fecha_ingreso': cell(hoja, 2, 9),
                'codigo2': cell(hoja, 9, 8)
                }


        libro_matriz.save('docs_generados/Matriz.xlsx')

import openpyxl

"""Supongo que con esto busoc manejar los informacion extraida y volcarlo al excel que tanto deseo"""

def create1():
    wb = openpyxl.Workbook()
    hoja = wb.active
    print(f'Hoja activa: {hoja.title}')

    hoja.title = "videos"
    print(f'Hoja activa: {wb.active.title}')

    wb.save('listadevideos.xlsx')

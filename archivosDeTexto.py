from io import open 


"""
archivo1 = open('archhivo.txt','a')
archivo1.write('\n saludo IDSG 801 nueva cosa')
archivo1.close()
"""
"""
print(leerArchivo.read())
leerArchivo.seek(10)
print(leerArchivo.read())
leerArchivo.close()
"""
leerArchivo = open('archhivo.txt','r')


for datos in leerArchivo.readlines():
    if 'saludo IDSG 801' == datos.rstrip():
        print(datos.rstrip())
leerArchivo.close()





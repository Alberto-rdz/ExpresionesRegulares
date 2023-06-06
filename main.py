import re
ER = '^b && a$'
#ER = '[b]\w+$'
cadena = input('Ingresa tu cadena: \n')
print('Tu cadena es: %s' % cadena)
x = re.search(ER,cadena)
print (x)

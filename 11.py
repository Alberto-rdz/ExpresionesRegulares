import re

print("\n11.Lenguaje de todas las  palabras que comienzan con b y terminan con a")
print("\nLa expresion es: A = b(aUb)*a")

cadena = input('Ingresa tu cadena: ')
print('Tu cadena es: %s' % cadena)

if re.fullmatch(r'^b[a-b]*a$', cadena):
  print("La cadena genera")
else:
  print("La cadena no se genera")

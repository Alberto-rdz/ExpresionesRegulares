import re

print("\n11.Lenguaje de todas las  palabras que comienzan con b y terminan con a")
print("\nLa expresion es: A= b(aUb)*a")

encontrado = "JALA"
NoEncontrado = "NO JALA"

cadena = input('Ingresa tu cadena: ')
print('Tu cadena es: %s' % cadena)
if re.fullmatch('(^b[a-b]*a$)', cadena):
  print(encontrado)
  input()
else:
  print(NoEncontrado)
  input()

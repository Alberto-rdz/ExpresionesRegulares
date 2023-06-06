import re

print("\n19.Lenguaje de todas las  palabras que tienen un número par de símbolos (longitud par)")
print("Sea el alfabeto Σ = {a,b,c} ")
print("\nLa expresion es: A = (ab)*(bc)*")

cadena = input('Ingresa tu cadena: ')
print('Tu cadena es: %s' % cadena)
#if re.fullmatch('^(([a-c]{2})*)$', cadena):
if re.fullmatch(r'(ab)*(bc)*', cadena):
  print("la cadena genera")
else:
  print("la cadena no se genera")
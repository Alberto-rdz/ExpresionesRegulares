import re

print("\n20.Lenguaje de todas las  palabras que tienen un número impar de símbolos (longitud impar)")
print("Sea el alfabeto Σ = {a,b,c} ")
print("\nLa expresion es: A = (aUbUc)*aUbUc ")
#((a+b+c)^2)*(a+b+c)
cadena = input('\nIngresa tu cadena: ')
print('Tu cadena es: %s' % cadena)
if re.fullmatch(r'([a-c]{2})*[a-c]', cadena):
  print("La cadena genera")
else:
  print("La cadena no se genera")

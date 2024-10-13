"""Tema: Control de flujo
uso de sentencias/condiciones if.elif,else
"""
print("################# Comparando numeros solo con if ############")
x = 5
x = 1
if x > 4:
  print("¡La condición era verdadera!")



# Diferente operador logico
p = 4
q = 2
if q != 0:
    print(p/q)

a = 4
b = 2
if b!= 0:
    e = a/b
    f = e + 1
    print(f)
print(e)
print(f)

if b != 0:
    c = a/b
    print("Dentro if")
print("Fuera if")


a = 10
if a > 5 and a < 15:
    print("Mayor que 5 y menos que 15")


numero = 4
if numero > 5 and numero < 15:
    print( numero > 5)
if numero >= 5:
    print(" no es mayor ni igual")
if numero <= 5:
    print(" si es menor")

print("################# Comparando numeros if and else ############")
y = 3
if y > 4:
  print("¡Es mayor a 4!") #esta sentencia no se ejecuta
else:
  print("¡No es verdadera, no es mayor a 4!") #esta sentencia se ejecuta


print("################# Comparando numeros if, elif, else ############")
list_ints = [1,2,3,4,5]
x = 5
if x == 5:
    print("Es 5")
elif x == 6:
    print("Es 6")
elif x == 7:
    print("Es 7")
else:
    print("No , el numero no es ninguna")

print("################# Comparando numeros si el usuario me da un numero ############")
number = int(input('Introduce un número: '))

if number > 0:
    print('Numero mayor a 0')
else:
    print('Numero menor a 0')

print('Linea fuera de if, elif, else')
print("################# Buscando un color todo el string############")

palabras = "Amarillo, Verde, Rojo, Naranja"
#palabra = "NaRanJa"
palabras = palabras.lower()

if "naranja" in palabras:
    print("Si hay color naranja")
else:
    print("No hay color naranja")
print("################# Buscando un color lista############")
# Reviso donde esta exactamente el color naranja por medio de lista
list_palabra = palabras.split()
color = list_palabra[3]
if "naranja" in color:
    print("Es color naranja")
else:
    print("No es color naranja")
import pdb
pdb.set_trace()


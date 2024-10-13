"""Ejercicio: Análisis de una Frase
Crea una variable que contenga una frase simple
Imprime la longitud de la cadena.
Encuentra cuantas palabras hay en la frase que anteriormente asignaste
Imprime una subcadena de la frase.
"""


##Fecha de creación: 12/octubre/2024##
##Crea una variable que contenga una frase simple##
Frase_inicial= "Hola mundo, esta es una frase inicial para el analisis de la misma"
##Imprime la longitud de la cadena.##
print(len(Frase_inicial))
##Encuentra cuantas palabras hay en la frase que anteriormente asignaste##
list_frase_inicial = list(Frase_inicial)
list_frase_palabras = Frase_inicial.split()
print("El numero de palabras encontradas es : " + str(len(list_frase_palabras)))

#Encuentran el numero de palabras por espacios
list_frase_palabras_dos = Frase_inicial.split(" ")
frase_de_salida = "El numero de palabras encontradas en segundo metodo por espacios es: "
numero_de_palabras = str(len(list_frase_palabras_dos))
print(frase_de_salida + numero_de_palabras)


# Quita espacios en blanco
print(frase_de_salida.replace(" ", ""))

#Imprime una subcadena de la frase.
trae_subcadena1 = Frase_inicial[0:5]
import pdb
pdb.set_trace()
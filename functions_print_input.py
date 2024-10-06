"""
Developer : cristina lugo
creation date : 21-sept-2024
Description: Program to learn basic concepts.
Updates: TBD
"""
# print() es una funcion propia de python, 
# recibe un parametro, se considera un salida, es decir retorna un valor
# el uso del signo \ es el union de linea de codigo.
# El uso de los caracteres \n nos da un salto de linea entre strings
print(" Welcome to course of Basic Knownlegde of \n Programming with Python \
      .......................................")

# Imprimiendo y concatenando un entero(int) que cambiamos a string el 5 previamente.
print("Only I am string ")
num_five = 5
print(num_five)
print ("Coverting this number to string " + str(num_five)) 

# input() es una funcion de entra, propia de python.
# permite recibir textos que el usuario escribe.
# Lo que recibe lo guardara como tipo string.
# se puede asignar a una variable.
name = input('What is your name?\n')
conc1 = 'Hola ' + name
print(conc1)
conc2 = name + ' please continue to fill the form'
print(conc2)
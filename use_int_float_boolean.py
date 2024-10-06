"""
this comments
Developer : cristina lugo
creation date : 14-sept-2024
Description: Program to learn: int, float, booleans.
Updates: 14-sep-2024
"""
###############################INTS###################################
# Ejemplos de asignacion de int.
# Números enteros, es decir positivos y negativos , no decimales.
age_carlos = 10
age_cristina = 15
decrease_pollution = -10
# para concatenar variables puedo usar el signo de + (variable1 + variable2)
# para poder imprimir estos valores con salto de linea (\n)
# debo cambiarlos a string porque el salto de linea es string y los ages no 
print("imprimiendo con salto de linea")
print(str(age_carlos) + "\n" + str(age_cristina))

# Tambien solo puedo imprimir todos estos numeros 
# juntos porque son todos son int
print("Imprimiendo solo los valores de variables")
print(age_cristina, age_carlos, decrease_pollution)

# Tambien puedo imprimir solo uno por uno solo
print("Imprimiendo solo los valores de variables")
print("Edad de cristina es:")
print(age_cristina)
print("Edad de carlos es:")
print(age_carlos)
print(" La contaminacion no tuvo decreción")
print(decrease_pollution)
# Revisando el tipo de datos int
type_age = type(age_cristina)
print("es de tipo " + str(type_age))

###############################FLOAT###################################
# Float es tipo decimal
decimalOne = 0.5
decimal_two = 1.5
negative_decimal = -10
print("Primer decimal")
print(decimalOne)
print("Segundo decinal")
print(decimalOne)
print("Concatena este numero decimal" + str(negative_decimal))
# Revisando el tipo de datos float
type_one = type(decimalOne)
type_two = type(decimal_two)
print("es de tipo " + str(decimalOne))
print("es de tipo " + str(decimal_two))


############################BOOLEANS######################################
bool_three = 'True'
# convirtiendo el string a boolean
bool_three = bool(bool_three)
bool_one = True
bool_two = False
# print boolean
print(bool_three)
print(bool_one)
print(bool_two)
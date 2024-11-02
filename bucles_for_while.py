"""
list_color = ["amarillo", "naranja", "azul" , "verde"]
for n_color in list_color:
    print(n_color)
    if "amarillo" in n_color:
        print("tu color favorito es el amarillo")


#print(list_color[0])
#print(list_color[1])
#print(list_color[2])

#range(4)
print("######## Imprimiendo colores por posiciones")
list_color = ["amarillo", "naranja", "azul" , "verde"]
#0,1,2,3
for n_color in range(len(list_color)):
    print(n_color)
    if n_color == 2:
        now_color = list_color[n_color]
        print("El color es azul")
        print(now_color)
    else:
        print("No es color azul")
        print(now_color)

"""
print("######## Imprimiendo una cadena de un correo")
# Revisar que sea un correo valido 
# Validar por medio de un for 
string_input = 'mi correo es el siguiente lugo1507@hotmail.com mi correo si tiene @' 
# correo valido es que:
# tenga @
# tenga .com
# resulto final : obtner el correo
list_string = string_input.split()
for n_string in list_string:
    print(n_string)
    if "@" in n_string:
        print("Revisando si es un correo")
        
        if ".com" in n_string and "hotmail" and len(n_string) > 1:
            print("Si es un correo")
            print(n_string)
        else:
            print(" No es un correo")
    else:
        print(" Esto tampoco es correo")


import pdb
pdb.set_trace()










"""
try:
    c = 5/0       # Si comentas esto entra en TypeError
    #d = 2 + "Hola" # Si comentas esto entra en ZeroDivisionError
except ZeroDivisionError:
    print("No se puede dividir entre cero!")

except TypeError:
    print("Problema de tipos!")


finally:
    print("Conitnua con el codigo")

print("Hello")

print(" debo continuar")
"""
abc = []
abc = []
xyz = {}
#print( "//" + nombre_varible)
color = "Amarillo"
try:
    # Aquí va el código que puede generar un error
    #resultado = 10 / 0  # Esto provocará un error de división por cero
    #d = "2" + "Hola"
    # Concatena los colores
    otro_color = "Azul"
    mas_colores = color + " " + otro_color
    print(mas_colores)
except Exception as e:
    print(f"Ocurrió un error: {e}")

print(mas_colores)

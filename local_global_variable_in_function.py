

# Tema principal :Revisar alcance variable
# Estas son variables globales ya que estan fuera de una funcion
last_name = "Lugo"
sent_name = ""

# Aqui podemos ver una variable local sent_name dentro de una funcion
# creada por nosotros
def print_names(sent_name):
    # this is my first fuction
    print("This is name " + sent_name)

# Acceder a mi funcion
exe = print_names("Cristina")
# Acceder a la funcion de palabra reservada llamada print()
exe1 = print("holaa")

# Usando un breakpoint o corte codigo con la libreria de pdb.
#import pdb
#pdb.set_trace()

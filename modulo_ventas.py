def opciones(opcion):

    if(opcion == 1):
        venta()

    elif(opcion == 2):
        print("\nsalir")

def venta():
    while(True):
        opcion = int(input(f"¿que estás buscando? :\n\n 1.Vuelos 2.Paquetes "))

        if(opcion == 2):
            print("feo")

paquetes = [{"nombre": "Todo Incluido", "detalle" : "Vuelo ida y regreso, Hotel, Barra libre, tour y transporte"}]

print("\nBienvenido al módulo de ventas........\n\n\n")
print("Opciones: \n\t1. Realizar una venta\n\t2. Salir")

seleccion = int(input("\nPor favor ingrese una de las opciones: "))

opciones(seleccion)
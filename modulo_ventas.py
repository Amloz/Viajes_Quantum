from Opciones_viajes import *
from Utilidades.clientes import *

def procesar_venta():
    print("\n---- Proceso de Venta ----")
    destino = seleccionar_destino()
    
    if destino:
        # Selección de la ciudad de salida
        print("\nSeleccione la ciudad desde donde desea viajar:")
        print("1. Bogotá\n2. Medellín\n3. Cali")
        ciudad = int(input("Ingrese el número correspondiente: "))
        
        if ciudad == 1:
            precio = Precio_viaje_BOG[destino]
            ciudad_origen = "Bogotá"
        elif ciudad == 2:
            precio = Precio_viaje_MED[destino]
            ciudad_origen = "Medellín"
        elif ciudad == 3:
            precio = Precio_viaje_CAL[destino]
            ciudad_origen = "Cali"
        else:
            print("Selección de ciudad no válida.")
            return
        
        # Capturas datos de las personas
        cliente = input("\nPor favor ingrese su nombre: ")

        # Confirmar la compra
        print(f"\nDestino: {destino}")
        print(f"Ciudad de salida: {ciudad_origen}")
        print(f"Precio del viaje: ${precio} COP")
        confirmar = input("¿Desea confirmar la compra? (s/n): ")
        
        if confirmar.lower() == 's':
            lista_clientes.append(cliente)
            print(f"\nVenta confirmada. Señor/a {cliente} Disfrute su viaje a {destino} desde {ciudad_origen}!")
        else:
            print("La venta ha sido cancelada.")
    else:
        print("No se ha podido procesar la venta.")


def opciones_venta():
    print("")
    print("--------------VIAJES QUAMTON------------------------")

    print("Explora el mundo a tu manera")

    print("\nSeleccione una de las opciones disponibles\n")
    print("1. Procesar una venta")
    print("2. ventas procesadas el día de hoy")
    print("3. Clientes registrados hoy")

    opcion = input("Seleccione una opcion (1 - 3): ")
    
    if opcion == "1" :
        procesar_venta()
    
    elif opcion == "2":
        conteo_ventas()
    
    elif opcion == "3":
        compras_durante_la_sesion()


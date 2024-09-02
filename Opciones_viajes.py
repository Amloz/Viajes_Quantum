from Utilidades.destinos import *

print("")
print("--------------VIAJES QUAMTON------------------------")

print("Explora el mundo a tu manera")

print("A continuacion se mostraran los destinos de viaje disponibles")


print("seleccione la ciudad la cual quiere visitar")


def seleccionar_destino():
    # Mostrar los destinos disponibles con un índice para seleccionarlos
    for i, destino in enumerate(Destinos):
        print(f"{i + 1}. {destino}")

    # Solicitar al usuario que seleccione un destino
    seleccion = int(input("Seleccione el número de la ciudad que desea visitar: ")) - 1

    if 0 <= seleccion < len(Destinos):
        destino_seleccionado = Destinos[seleccion]
        dia_disponible = Dias[seleccion % len(Dias)]  # Selección de un día basado en el índice
        horario_disponible = Horarios[seleccion % len(Horarios)]  # Selección de un horario basado en el índice
        precioBG = Precio_viaje_BOG[destino_seleccionado] #Precio diccionario desde una sede en Bogota
        precioMD = Precio_viaje_MED[destino_seleccionado] #Precio diccionario desde una sede en Medellin
        precioCA = Precio_viaje_CAL[destino_seleccionado] #Precio diccionario desde una sede en Cali

        print(f"\nDestino seleccionado: {destino_seleccionado}")
        print(f"Día disponible para viajar a ", destino_seleccionado, ":" ,dia_disponible, "")
        print(f"Horario de salida: {horario_disponible}")
        print(f"Precio del viaje desde Bogotá a {destino_seleccionado} : ${precioBG} COP")
        print(f"Precio del viaje desde Medellin a {destino_seleccionado} : ${precioMD} COP")
        print(f"Precio del viaje desde Cali a {destino_seleccionado} : ${precioCA} COP")
    else:
        print("Por favor, seleccione uno de las opciones que se muestran arriba.")
        

seleccionar_destino()




print("")
print("--------------VIAJES QUAMTON------------------------")

print("Explora el mundo a tu manera")

print("A continuacion se mostraran los destinos de viaje disponibles")


print("seleccione la ciudad la cual quiere visitar")

#Destinos disponibles
Destinos = ["Buenos Aires(Argentina)","Mexico DC(Mexico)","Berlin(Alemania)", "Atenas(Grecia)", 
            "Roma(Italia)", "Florencia(Italia)",  "Orlando(USA)", "New York(USA)", 
            "Santo Domingo(RD)", "Manchester(Inglaterra)",  "Londres(Inglaterra)", "Dublin(Irlanda)", 
            "Paris(Francia)", "Madrid(España)", "Praga(Republica Checa)","Tokio(Japon)","Estambul(Turquia)","Lisboa(Portugal)","Oporto(Portugal)", "Lima(Peru)","Rio de Janeiro(Brasil)"]

Dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

#Horarios disponibles

Horarios = ["8:00 am","9:00 am","10:00 am","11:00 am","11:30 am","1:00 pm", "2:00 pm","2:30 pm","2:50 pm","3:20 pm", "4:00 pm","6:00 pm","6:15 pm","6:30 pm","6:45 pm","7:15 pm", "8:00 pm","8:30 pm", "9:00 pm"]


#Diccionario para los precios de los viajes desde Bogota a destino
Precio_viaje_BOG = {
    "Buenos Aires(Argentina)": 1200700,
    "Mexico DC(Mexico)": 1400000,
    "Berlin(Alemania)": 6609000, 
    "Atenas(Grecia)": 8800600, 
    "Roma(Italia)": 7000980, 
    "Florencia(Italia)": 7200000, 
    "Orlando(USA)": 720000,
    "New York(USA)": 2100000, 
    "Santo Domingo(RD)": 833650, 
    "Manchester(Inglaterra)": 7111500,  
    "Londres(Inglaterra)": 7101000,
    "Dublin(Irlanda)": 6500000, 
    "Paris(Francia)": 6543030, 
    "Madrid(España)": 5430330, 
    "Praga(Republica Checa)" :4039200 ,
    "Tokio(Japon)":3311980,
    "Estambul(Turquia)": 5101670,
    "Lisboa(Portugal)": 5180493,
    "Oporto(Portugal)": 5230203,
    "Lima(Peru)": 714000,
    "Rio de Janeiro(Brasil)": 1161862
    
}

#Diccionario para los precios de los viajes desde Cali a destino
Precio_viaje_CAL = {
    "Buenos Aires(Argentina)": 1592600,
    "Mexico DC(Mexico)": 1272900,
    "Berlin(Alemania)": 4808694, 
    "Atenas(Grecia)": 4604594, 
    "Roma(Italia)": 6400980, 
    "Florencia(Italia)": 6700000, 
    "Orlando(USA)": 1340403,
    "New York(USA)": 2391504, 
    "Santo Domingo(RD)": 1709584, 
    "Manchester(Inglaterra)": 5403933,  
    "Londres(Inglaterra)": 5921000,
    "Dublin(Irlanda)": 4554500, 
    "Paris(Francia)": 6723030, 
    "Madrid(España)": 6280594, 
    "Praga(Republica Checa)" :4209200 ,
    "Tokio(Japon)":2894039,
    "Estambul(Turquia)": 3904594,
    "Lisboa(Portugal)": 4650594,
    "Oporto(Portugal)": 5000203,
    "Lima(Peru)": 893000,
    "Rio de Janeiro(Brasil)": 1655862
    
}

#Diccionario para los precios de los viajes desde Medellin a destino
Precio_viaje_MED = {
    "Buenos Aires(Argentina)": 1613400,
    "Mexico DC(Mexico)": 1108000,
    "Berlin(Alemania)": 4666306, 
    "Atenas(Grecia)": 44560493, 
    "Roma(Italia)": 7210980, 
    "Florencia(Italia)": 7761000, 
    "Orlando(USA)": 920600,
    "New York(USA)": 2300100, 
    "Santo Domingo(RD)": 928450, 
    "Manchester(Inglaterra)": 4504948,  
    "Londres(Inglaterra)": 3707560,
    "Dublin(Irlanda)": 6202000, 
    "Paris(Francia)": 6252630, 
    "Madrid(España)": 5813630, 
    "Praga(Republica Checa)" :4097500 ,
    "Tokio(Japon)":2849670,
    "Estambul(Turquia)": 4607678,
    "Lisboa(Portugal)": 6180493,
    "Oporto(Portugal)": 6540392,
    "Lima(Peru)": 735500,
    "Rio de Janeiro(Brasil)": 1690802
    
}

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


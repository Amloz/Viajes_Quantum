
import tkinter as tk
from tkinter import ttk, messagebox

# Listas
Destinos = [
    "Buenos Aires(Argentina)", "Mexico DC(Mexico)", "Berlin(Alemania)", "Atenas(Grecia)",
    "Roma(Italia)", "Florencia(Italia)", "Orlando(USA)", "New York(USA)",
    "Santo Domingo(RD)", "Manchester(Inglaterra)", "Londres(Inglaterra)", "Dublin(Irlanda)",
    "Paris(Francia)", "Madrid(España)", "Praga(Republica Checa)", "Tokio(Japon)", "Estambul(Turquia)",
    "Lisboa(Portugal)", "Oporto(Portugal)", "Lima(Peru)", "Rio de Janeiro(Brasil)"
]

Dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

Horarios = [
    "8:00 am", "9:00 am", "10:00 am", "11:00 am", "11:30 am", "1:00 pm",
    "2:00 pm", "2:30 pm", "2:50 pm", "3:20 pm", "4:00 pm", "6:00 pm",
    "6:15 pm", "6:30 pm", "6:45 pm", "7:15 pm", "8:00 pm", "8:30 pm", "9:00 pm"
]

# Diccionarios para los precios de los viajes desde Bogota
Precio_viaje_BOG = {
    "Buenos Aires(Argentina)": 1200700, "Mexico DC(Mexico)": 1400000, "Berlin(Alemania)": 6609000,
    "Atenas(Grecia)": 8800600, "Roma(Italia)": 7000980, "Florencia(Italia)": 7200000,
    "Orlando(USA)": 720000, "New York(USA)": 2100000, "Santo Domingo(RD)": 833650,
    "Manchester(Inglaterra)": 7111500, "Londres(Inglaterra)": 7101000, "Dublin(Irlanda)": 6500000,
    "Paris(Francia)": 6543030, "Madrid(España)": 5430330, "Praga(Republica Checa)": 4039200,
    "Tokio(Japon)": 3311980, "Estambul(Turquia)": 5101670, "Lisboa(Portugal)": 5180493,
    "Oporto(Portugal)": 5230203, "Lima(Peru)": 714000, "Rio de Janeiro(Brasil)": 1161862
}

# Diccionarios para los precios de los viajes desde Cali
Precio_viaje_CAL = {
    "Buenos Aires(Argentina)": 1592600, "Mexico DC(Mexico)": 1272900, "Berlin(Alemania)": 4808694,
    "Atenas(Grecia)": 4604594, "Roma(Italia)": 6400980, "Florencia(Italia)": 6700000,
    "Orlando(USA)": 1340403, "New York(USA)": 2391504, "Santo Domingo(RD)": 1709584,
    "Manchester(Inglaterra)": 5403933, "Londres(Inglaterra)": 5921000, "Dublin(Irlanda)": 4554500,
    "Paris(Francia)": 6723030, "Madrid(España)": 6280594, "Praga(Republica Checa)": 4209200,
    "Tokio(Japon)": 2894039, "Estambul(Turquia)": 3904594, "Lisboa(Portugal)": 4650594,
    "Oporto(Portugal)": 5000203, "Lima(Peru)": 893000, "Rio de Janeiro(Brasil)": 1655862
}

# Diccionarios para los precios de los viajes desde Medellin
Precio_viaje_MED = {
    "Buenos Aires(Argentina)": 1613400, "Mexico DC(Mexico)": 1108000, "Berlin(Alemania)": 4666306,
    "Atenas(Grecia)": 44560493, "Roma(Italia)": 7210980, "Florencia(Italia)": 7761000,
    "Orlando(USA)": 920600, "New York(USA)": 2300100, "Santo Domingo(RD)": 928450,
    "Manchester(Inglaterra)": 4504948, "Londres(Inglaterra)": 3707560, "Dublin(Irlanda)": 6202000,
    "Paris(Francia)": 6252630, "Madrid(España)": 5813630, "Praga(Republica Checa)": 4097500,
    "Tokio(Japon)": 2849670, "Estambul(Turquia)": 4607678, "Lisboa(Portugal)": 6180493,
    "Oporto(Portugal)": 6540392, "Lima(Peru)": 735500, "Rio de Janeiro(Brasil)": 1690802
}

def seleccionar_destino():
    
    seleccion = lista_destinos.get()

    if seleccion:
        dia_disponible = Dias[Destinos.index(seleccion) % len(Dias)]
        horario_disponible = Horarios[Destinos.index(seleccion) % len(Horarios)]
        precioBG = Precio_viaje_BOG[seleccion]
        precioMD = Precio_viaje_MED[seleccion]
        precioCA = Precio_viaje_CAL[seleccion]

        # Mostrar mensaje con la información seleccionada
        mensaje = f"Destino seleccionado: {seleccion}\n"
        mensaje += f"Día disponible para viajar: {dia_disponible}\n"
        mensaje += f"Horario de salida: {horario_disponible}\n"
        mensaje += f"Precio del viaje desde Bogotá: ${precioBG} COP\n"
        mensaje += f"Precio del viaje desde Medellin: ${precioMD} COP\n"
        mensaje += f"Precio del viaje desde Cali: ${precioCA} COP"
        
        messagebox.showinfo("Información de Viaje", mensaje)
    else:
        messagebox.showwarning("Selección inválida", "Por favor, selecciona un destino.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Viajes Quamton")
ventana.geometry("400x300")

# Crear y colocar etiquetas
etiqueta = tk.Label(ventana, text="--------------VIAJES QUAMTON------------------------\nExplora el mundo a tu manera\nSelecciona la ciudad que quieres visitar", font=("Arial", 12))
etiqueta.pack(pady=10)

# Crear y colocar la lista de destinos
lista_destinos = ttk.Combobox(ventana, values=Destinos, font=("Arial", 10))
lista_destinos.pack(pady=10)

# Crear y colocar el botón para seleccionar el destino
boton_seleccionar = tk.Button(ventana, text="Seleccionar Destino", font=("Arial", 12), command=seleccionar_destino)
boton_seleccionar.pack(pady=20)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()

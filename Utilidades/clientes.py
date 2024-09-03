lista_clientes = []


def compras_durante_la_sesion():
    print("\nLos clientes que han realizado una reservación el día de hoy son: \n")

    if len(lista_clientes) == 0:
        print("\nEl día de hoy no se han realizado ventas")

    else :
        for i in lista_clientes:
            print(i)

        print("\n")

def conteo_ventas():
    if len(lista_clientes) == 0:
        print("\nEl día de hoy no se han realizado ventas")
    
    else:
        print(f"\nLa cantidad de ventas procesadas durante la sesión es: {len(lista_clientes)}\n")


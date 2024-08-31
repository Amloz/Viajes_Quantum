# Agencia de viajes Quantum
destinos = ['a', 'b', 'c'] #adjuntar destinos

def mostrar_menu_principal():
    
    print("*      Agencia de Viajes Quantum       *")
    print("     ¡Explora el mundo a tu manera!")
    print("1. Explorar Quantum")
    

def entrar_menu_principal():
    while True:
        
        print("*      Menú Principal          *")
       
        print("1. Gestionar destinos")
        print("2. Buscar destino")
        print("3. Quiénes somos nosotros")
        print("4. Regresar")
      
        opcion = input("Seleccione una opción (1-4): ")
        if opcion == '1':
            gestionar_destinos()
        elif opcion == '2':
            buscar_destino()
        elif opcion == '3':
            quienes_somos()
        elif opcion == '4':
            break  # Volver al menú principal
        else:
            print("Opción no válida, por favor seleccione una opción del 1 al 4.")

def gestionar_destinos():
    while True:
        print("*       Gestión de Destinos    *")
        
        print("1. Ver destinos")
        print("2. Volver al menú principal")
       
        opcion = input("*Seleccione una opción (1-2)*: ")        
        if opcion == '1':
            if destinos:
                print("Destinos disponibles:")
                for i, destino in enumerate(destinos, start=1):
                    print(f"{i}. {destino}")
                input("Presione Enter para volver al menú principal.")
            else:
                print("No hay destinos disponibles.")
                input("Presione Enter para volver al menú principal.")
        elif opcion == '2':
            break  # Volver al menú principal
        else:
            print("Opción no válida, por favor seleccione una opción del 1 al 2.")

def buscar_destino():
    destino_buscado = input("Ingrese el destino que desea buscar: ")
    if destino_buscado in destinos:
        print(f"Destino '{destino_buscado}' disponible, puedes consultar los detalles de {destino_buscado}.")
    else:
        print("Destino no disponible, por el momento no tenemos cobertura en este destino.")
    # Regresar al menú principal automáticamente
    input("Presione Enter para volver al menú principal.")
    return

def quienes_somos():

    print("*      Quiénes somos           *")
  
    print("En Agencia de Viajes Quantum, creemos que cada viaje es una oportunidad para descubrir,")
    print("soñar y explorar el mundo de una manera única. Ofrecemos destinos exclusivos y experiencias")
    print("inolvidables que se adaptan a tus deseos y necesidades. ¡Viaja con nosotros y haz realidad")
    print("tus sueños de aventura!")
    input("Presione Enter para volver al menú principal.")

def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Ingresa presionando 1: ")

        if opcion == '1':
            print("Gracias por mostrar interés en la agencia de viajes Quantum.") 
            entrar_menu_principal()                       
        else:
            print("Opción no válida, por favor seleccione una opción valida.")

if __name__ == "__main__":
    main()

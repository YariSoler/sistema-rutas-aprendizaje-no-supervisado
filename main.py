from conocimiento import obtener_estaciones
from reglas import validar_ruta
from busqueda import encontrar_ruta


def mostrar_estaciones(estaciones):
   

    print("\nEstaciones disponibles:")

    for numero, estacion in enumerate(estaciones, start=1):
        print(f"{numero}. {estacion}")


def mostrar_ruta(ruta):
    

    print("\nRUTA ENCONTRADA\n")

    for i, estacion in enumerate(ruta):

        if i < len(ruta) - 1:
            print(f"{estacion} ↓")
        else:
            print(estacion)

    print("\nNúmero de desplazamientos:", len(ruta) - 1)


def main():

    print("==========================================")
    print("       SISTEMA INTELIGENTE DE RUTAS")
    print("==========================================")

    estaciones = obtener_estaciones()

    mostrar_estaciones(estaciones)

    print("\n------------------------------------------")

    origen = input("\nIngrese la estación de origen: ").strip()
    destino = input("Ingrese la estación de destino: ").strip()

    print("\n------------------------------------------")

   
    if not validar_ruta(origen, destino, estaciones):

        print("\nNo se puede realizar la búsqueda.")

        if origen not in estaciones:
            print(f"El origen '{origen}' no pertenece a la base de conocimiento.")

        if destino not in estaciones:
            print(f"El destino '{destino}' no pertenece a la base de conocimiento.")

        return


    ruta = encontrar_ruta(origen, destino, mostrar_proceso=True)

    if ruta:

        mostrar_ruta(ruta)

    else:

        print("\nNo fue posible encontrar una ruta entre las estaciones seleccionadas.")

    print("\n------------------------------------------")


if __name__ == "__main__":
    main()
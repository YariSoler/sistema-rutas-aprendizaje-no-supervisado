
from conocimiento import obtener_estaciones
from reglas import validar_ruta
from busqueda import encontrar_ruta
from modelo_supervisado import entrenar_modelo, predecir_duracion
from modelo_no_supervisado import (
    entrenar_modelo as entrenar_modelo_no_supervisado,
)


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


def buscar_ruta():
    estaciones = obtener_estaciones()
    mostrar_estaciones(estaciones)

    print("\n------------------------------------------")

    origen_numero = input(
        "\nIngrese el número de la estación de origen: "
    ).strip()

    destino_numero = input(
        "Ingrese el número de la estación de destino: "
    ).strip()

    try:
        origen_numero = int(origen_numero)
        destino_numero = int(destino_numero)

    except ValueError:
        print("\nDebe ingresar números de estación válidos.")
        return

    if not 1 <= origen_numero <= len(estaciones):
        print("\nEl número de origen no es válido.")
        return

    if not 1 <= destino_numero <= len(estaciones):
        print("\nEl número de destino no es válido.")
        return

    origen = estaciones[origen_numero - 1]
    destino = estaciones[destino_numero - 1]

    print("\n------------------------------------------")
    print(f"\nOrigen seleccionado: {origen}")
    print(f"Destino seleccionado: {destino}")
    print("\n------------------------------------------")

    if not validar_ruta(origen, destino, estaciones):
        print("\nNo se puede realizar la búsqueda.")
        return

    ruta = encontrar_ruta(
        origen,
        destino,
        mostrar_proceso=True,
    )

    if ruta:
        mostrar_ruta(ruta)
    else:
        print(
            "\nNo fue posible encontrar una ruta "
            "entre las estaciones seleccionadas."
        )


def realizar_prediccion():
    print("\n==========================================")
    print("       PREDICCIÓN DE DURACIÓN")
    print("==========================================")

    try:
        hora = int(input("\nIngrese la hora del viaje (0-23): "))

        if not 0 <= hora <= 23:
            print("\nLa hora debe estar entre 0 y 23.")
            return

        dia_semana = int(
            input(
                "Ingrese el día de la semana "
                "(0=Lunes, 1=Martes, ..., 6=Domingo): "
            )
        )

        if not 0 <= dia_semana <= 6:
            print("\nEl día debe estar entre 0 y 6.")
            return

        pasajeros = int(
            input("Ingrese la cantidad de pasajeros: ")
        )

        if pasajeros <= 0:
            print(
                "\nLa cantidad de pasajeros "
                "debe ser mayor que 0."
            )
            return

        distancia_km = float(
            input("Ingrese la distancia del recorrido (km): ")
        )

        if distancia_km <= 0:
            print("\nLa distancia debe ser mayor que 0.")
            return

        numero_paradas = int(
            input("Ingrese el número de paradas: ")
        )

        if numero_paradas <= 0:
            print("\nEl número de paradas debe ser mayor que 0.")
            return

        print("\nEntrenando modelo supervisado...")

        modelo, mae, mse, r2 = entrenar_modelo()

        prediccion = predecir_duracion(
            modelo,
            hora,
            dia_semana,
            pasajeros,
            distancia_km,
            numero_paradas,
        )

        print("\n------------------------------------------")
        print("RESULTADO DE LA PREDICCIÓN")
        print("------------------------------------------")

        print(f"Duración estimada: {prediccion:.1f} minutos")

        print("\nMétricas del modelo:")
        print(f"MAE: {mae:.2f} minutos")
        print(f"MSE: {mse:.2f}")
        print(f"R²: {r2:.2f}")

    except ValueError:
        print("\nError: ingrese un valor numérico válido.")


def agrupar_viajes():
    print("\n==========================================")
    print("       AGRUPAMIENTO DE VIAJES CON K-MEANS")
    print("==========================================")

    try:
        (
            modelo,
            resultados,
            inercia,
            silueta,
        ) = entrenar_modelo_no_supervisado()

        print("\nRESUMEN DEL AGRUPAMIENTO")
        print("------------------------------------------")

        for grupo, datos_grupo in resultados.groupby("grupo"):
            print(f"\nGrupo {grupo}:")
            print(f"Cantidad de viajes: {len(datos_grupo)}")
            print(
                f"Pasajeros promedio: "
                f"{datos_grupo['pasajeros'].mean():.2f}"
            )
            print(
                f"Distancia promedio: "
                f"{datos_grupo['distancia_km'].mean():.2f} km"
            )
            print(
                f"Paradas promedio: "
                f"{datos_grupo['numero_paradas'].mean():.2f}"
            )
            print(
                f"Duración promedio: "
                f"{datos_grupo['duracion_min'].mean():.2f} minutos"
            )

        print("\nMÉTRICAS DEL AGRUPAMIENTO")
        print("------------------------------------------")
        print(f"Inercia: {inercia:.2f}")
        print(f"Coeficiente de silueta: {silueta:.3f}")

        print(
            "\nLos resultados completos están guardados en "
            "datos/resultados_agrupamiento.csv"
        )

    except (FileNotFoundError, ValueError) as error:
        print(f"\nNo fue posible realizar el agrupamiento: {error}")


def main():
    while True:
        print("\n==========================================")
        print("       SISTEMA INTELIGENTE DE RUTAS")
        print("==========================================")

        print("\n1. Buscar mejor ruta")
        print("2. Predecir duración del viaje")
        print("3. Agrupar viajes con K-Means")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            buscar_ruta()

        elif opcion == "2":
            realizar_prediccion()

        elif opcion == "3":
            agrupar_viajes()

        elif opcion == "4":
            print(
                "\nGracias por utilizar "
                "el sistema inteligente de rutas."
            )
            break

        else:
            print("\nOpción no válida. Seleccione del 1 al 4.")


if __name__ == "__main__":
    main()

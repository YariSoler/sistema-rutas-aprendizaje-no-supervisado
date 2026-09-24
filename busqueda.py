import heapq

from conocimiento import conexiones, obtener_posicion


def heuristica(estacion_actual, destino):

    posicion_actual = obtener_posicion(estacion_actual)
    posicion_destino = obtener_posicion(destino)

    if posicion_actual is None or posicion_destino is None:
        return float("inf")

    return abs(posicion_actual - posicion_destino)


def encontrar_ruta(origen, destino, mostrar_proceso=False):

    frontera = []
    h_origen = heuristica(origen, destino)


    f_origen = 0 + h_origen

    heapq.heappush(
        frontera,
        (f_origen, 0, origen, [origen])
    )

    costos = {
        origen: 0
    }


    if mostrar_proceso:

        print("\n==========================================")
        print("             PROCESO A*")
        print("==========================================")


    while frontera:


        f_actual, costo_actual, estacion_actual, ruta_actual = heapq.heappop(
            frontera
        )

        h_actual = heuristica(
            estacion_actual,
            destino
        )


        if mostrar_proceso:

            print("\nEstación evaluada:", estacion_actual)
            print("g(n) =", costo_actual)
            print("h(n) =", h_actual)
            print("f(n) =", f_actual)

  
        if estacion_actual == destino:

            return ruta_actual

        for vecino in conexiones.get(estacion_actual, []):

        
            nuevo_costo = costo_actual + 1

          
            if vecino not in costos or nuevo_costo < costos[vecino]:

                costos[vecino] = nuevo_costo

                h = heuristica(
                    vecino,
                    destino
                )

                f = nuevo_costo + h

        
                nueva_ruta = ruta_actual + [vecino]

                heapq.heappush(
                    frontera,
                    (f, nuevo_costo, vecino, nueva_ruta)
                )


    return None
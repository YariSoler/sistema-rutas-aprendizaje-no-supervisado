
from conocimiento import estan_conectadas


def validar_estacion(estacion, estaciones):
 

    return estacion in estaciones


def puede_desplazarse(origen, destino):
   

    return estan_conectadas(origen, destino)


def validar_ruta(origen, destino, estaciones):
   

    origen_valido = validar_estacion(origen, estaciones)
    destino_valido = validar_estacion(destino, estaciones)

    if origen_valido and destino_valido:
        return True

    return False
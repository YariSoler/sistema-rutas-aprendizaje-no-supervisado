conexiones = {

    "Portal Américas": [
        "Banderas"
    ],

    "Banderas": [
        "Portal Américas",
        "Mundo Aventura"
    ],

    "Mundo Aventura": [
        "Banderas",
        "Pradera"
    ],

    "Pradera": [
        "Mundo Aventura",
        "Marsella"
    ],

    "Marsella": [
        "Pradera",
        "Distrito Graffiti"
    ],

    "Distrito Graffiti": [
        "Marsella",
        "Puente Aranda"
    ],

    "Puente Aranda": [
        "Distrito Graffiti",
        "Zona Industrial"
    ],

    "Zona Industrial": [
        "Puente Aranda",
        "Ricaurte"
    ],

    "Ricaurte": [
        "Zona Industrial",
        "De La Sabana"
    ],

    "De La Sabana": [
        "Ricaurte",
        "Avenida Jiménez"
    ],

    "Avenida Jiménez": [
        "De La Sabana",
        "Calle 19"
    ],

    "Calle 19": [
        "Avenida Jiménez",
        "Calle 26"
    ],

    "Calle 26": [
        "Calle 19",
        "Universidades",
        "Calle 72"
    ],

    "Universidades": [
        "Calle 26"
    ],

    "Calle 72": [
        "Calle 26",
        "Portal Norte"
    ],

    "Portal Norte": [
        "Calle 72"
    ]
    
}

posiciones = {

    "Portal Américas": 0,
    "Banderas": 1,
    "Mundo Aventura": 2,
    "Pradera": 3,
    "Marsella": 4,
    "Distrito Graffiti": 5,
    "Puente Aranda": 6,
    "Zona Industrial": 7,
    "Ricaurte": 8,
    "De La Sabana": 9,
    "Avenida Jiménez": 10,
    "Calle 19": 11,
    "Calle 26": 12,
    "Universidades": 13,
    "Calle 72": 13,
    "Portal Norte": 14
}


def obtener_estaciones():
   
    return list(conexiones.keys())


def estan_conectadas(origen, destino):

    return destino in conexiones.get(origen, [])


def obtener_posicion(estacion):
  
    return posiciones.get(estacion)

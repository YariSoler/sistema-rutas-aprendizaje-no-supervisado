
import csv
import random
from pathlib import Path

random.seed(42)

CARPETA_DATOS = Path(__file__).parent
ARCHIVO_SALIDA = CARPETA_DATOS / "dataset_agrupamiento.csv"


def generar_dataset():
   

    viajes = []

  
    perfiles = [
        {
            "nombre": "viaje_corto",
            "pasajeros": (10, 80),
            "distancia": (1.0, 5.0),
            "paradas": (1, 4),
            "duracion": (5, 25),
        },
        {
            "nombre": "viaje_medio",
            "pasajeros": (60, 180),
            "distancia": (4.0, 12.0),
            "paradas": (3, 9),
            "duracion": (20, 50),
        },
        {
            "nombre": "viaje_largo",
            "pasajeros": (150, 350),
            "distancia": (10.0, 25.0),
            "paradas": (7, 16),
            "duracion": (40, 90),
        },
    ]

  
    for perfil in perfiles:
        for _ in range(50):
            viajes.append({
                "pasajeros": random.randint(
                    *perfil["pasajeros"]
                ),
                "distancia_km": round(
                    random.uniform(*perfil["distancia"]), 2
                ),
                "numero_paradas": random.randint(
                    *perfil["paradas"]
                ),
                "duracion_min": random.randint(
                    *perfil["duracion"]
                ),
            })

   
    random.shuffle(viajes)

    with open(
        ARCHIVO_SALIDA,
        "w",
        newline="",
        encoding="utf-8",
    ) as archivo:
        campos = [
            "pasajeros",
            "distancia_km",
            "numero_paradas",
            "duracion_min",
        ]

        escritor = csv.DictWriter(
            archivo,
            fieldnames=campos,
        )
        escritor.writeheader()
        escritor.writerows(viajes)

    print("Conjunto de datos generado correctamente.")
    print(f"Cantidad de registros: {len(viajes)}")
    print(f"Archivo creado: {ARCHIVO_SALIDA}")
    print("Origen: datos sintéticos para fines académicos.")


if __name__ == "__main__":
    generar_dataset()

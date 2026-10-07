import csv
import random

random.seed(42)

dias = {
    "Lunes": 0,
    "Martes": 1,
    "Miercoles": 2,
    "Jueves": 3,
    "Viernes": 4,
    "Sabado": 5,
    "Domingo": 6
}

registros = []

for _ in range(150):
    hora = random.randint(5, 22)
    dia_nombre = random.choice(list(dias.keys()))
    dia_semana = dias[dia_nombre]

    pasajeros = random.randint(50, 300)
    distancia_km = round(random.uniform(2.0, 12.0), 1)
    numero_paradas = random.randint(2, 10)

    # Mayor cantidad de pasajeros y horas pico aumentan el tiempo.
    factor_hora = 0

    if 6 <= hora <= 9:
        factor_hora = 6
    elif 17 <= hora <= 20:
        factor_hora = 8
    elif 10 <= hora <= 16:
        factor_hora = 2

    factor_dia = 3 if dia_semana in [0, 4] else 0

    duracion = (
        5
        + (distancia_km * 2.5)
        + (numero_paradas * 1.8)
        + (pasajeros * 0.025)
        + factor_hora
        + factor_dia
        + random.uniform(-2, 2)
    )

    duracion_min = round(max(duracion, 8), 1)

    registros.append([
        hora,
        dia_semana,
        pasajeros,
        distancia_km,
        numero_paradas,
        duracion_min
    ])


with open("datos/dataset_transporte.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)

    escritor.writerow([
        "hora",
        "dia_semana",
        "pasajeros",
        "distancia_km",
        "numero_paradas",
        "duracion_min"
    ])

    escritor.writerows(registros)

print("Dataset generado correctamente.")
print(f"Cantidad de registros: {len(registros)}")
print("Archivo creado: datos/dataset_transporte.csv")
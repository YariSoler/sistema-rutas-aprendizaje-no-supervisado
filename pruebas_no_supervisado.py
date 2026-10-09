
from pathlib import Path

import pandas as pd

from modelo_no_supervisado import entrenar_modelo


def ejecutar_pruebas():
    print("\n========== PRUEBAS DEL MODELO NO SUPERVISADO ==========")

  
    archivo_datos = (
        Path(__file__).parent
        / "datos"
        / "dataset_agrupamiento.csv"
    )

    assert archivo_datos.exists(), (
        "ERROR: no existe el conjunto de datos."
    )
    print("PRUEBA 1 APROBADA: el conjunto de datos existe.")

   
    datos = pd.read_csv(archivo_datos)

    assert len(datos) == 150, (
        f"Se esperaban 150 registros, se encontraron {len(datos)}."
    )
    print("PRUEBA 2 APROBADA: hay 150 registros.")

   
    columnas = {
        "pasajeros",
        "distancia_km",
        "numero_paradas",
        "duracion_min",
    }

    assert columnas.issubset(datos.columns), (
        "Faltan columnas necesarias en el conjunto de datos."
    )
    print("PRUEBA 3 APROBADA: las columnas requeridas existen.")

   
    modelo, resultados, inercia, silueta = entrenar_modelo()

    assert len(resultados) == 150, (
        "El modelo no procesó los 150 viajes."
    )
    print("PRUEBA 4 APROBADA: el modelo procesó los 150 viajes.")

    assert resultados["grupo"].nunique() == 3, (
        "El modelo no generó los tres grupos esperados."
    )
    print("PRUEBA 5 APROBADA: se identificaron tres grupos.")

    assert resultados["grupo"].notna().all(), (
        "Hay viajes sin grupo asignado."
    )
    print("PRUEBA 6 APROBADA: todos los viajes tienen grupo.")

    assert inercia >= 0, "La inercia no puede ser negativa."
    assert -1 <= silueta <= 1, (
        "El coeficiente de silueta está fuera del rango esperado."
    )
    print("PRUEBA 7 APROBADA: las métricas están en rangos válidos.")

    archivo_resultados = (
        Path(__file__).parent
        / "datos"
        / "resultados_agrupamiento.csv"
    )

    assert archivo_resultados.exists(), (
        "No se generó el archivo de resultados."
    )
    print("PRUEBA 8 APROBADA: el archivo de resultados existe.")

    print("\nRESULTADO FINAL: todas las pruebas fueron aprobadas.")


if __name__ == "__main__":
    ejecutar_pruebas()

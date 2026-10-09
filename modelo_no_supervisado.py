
from pathlib import Path

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score



RUTA_DATOS = (
    Path(__file__).parent
    / "datos"
    / "dataset_agrupamiento.csv"
)


def entrenar_modelo():

    if not RUTA_DATOS.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo de datos: {RUTA_DATOS}\n"
            "Primero debes generar el conjunto de datos."
        )

    datos = pd.read_csv(RUTA_DATOS)

 
    columnas = [
        "pasajeros",
        "distancia_km",
        "numero_paradas",
        "duracion_min",
    ]


    faltantes = [col for col in columnas if col not in datos.columns]

    if faltantes:
        raise ValueError(
            f"Faltan las siguientes columnas en el CSV: {faltantes}"
        )

 
    X = datos[columnas].copy()

    if X.isnull().any().any():
        raise ValueError(
            "El conjunto de datos contiene valores vacíos."
        )

    if len(X) < 4:
        raise ValueError(
            "Se necesitan al menos 4 viajes para realizar el agrupamiento."
        )

    
    escalador = StandardScaler()
    X_escalado = escalador.fit_transform(X)

   
    modelo = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10,
    )

    grupos = modelo.fit_predict(X_escalado)

   
    resultados = datos.copy()
    resultados["grupo"] = grupos

  
    inercia = modelo.inertia_
    silueta = silhouette_score(X_escalado, grupos)

    print("\n========== MODELO NO SUPERVISADO ==========")
    print("Algoritmo: K-Means")
    print(f"Cantidad de viajes analizados: {len(datos)}")
    print("Cantidad de grupos: 3")
    print(f"Inercia: {inercia:.2f}")
    print(f"Coeficiente de silueta: {silueta:.3f}")

    print("\n========== VIAJES AGRUPADOS ==========")
    print(resultados.to_string(index=False))

    print("\n========== RESUMEN DE LOS GRUPOS ==========")
    resumen = resultados.groupby("grupo")[columnas].mean().round(2)
    print(resumen)


    ruta_resultados = (
        Path(__file__).parent
        / "datos"
        / "resultados_agrupamiento.csv"
    )

    resultados.to_csv(ruta_resultados, index=False)

    print(f"\nResultados guardados en: {ruta_resultados}")

    return modelo, resultados, inercia, silueta


if __name__ == "__main__":
    entrenar_modelo()
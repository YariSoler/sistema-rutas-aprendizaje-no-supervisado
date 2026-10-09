Sistema Inteligente de Rutas con Aprendizaje Supervisado y No Supervisado

PDF:

[descripcion_datos_no_supervisado.pdf](https://github.com/user-attachments/files/33232740/descripcion_datos_no_supervisado.pdf)[pruebas_no_supervisado.pdf](https://github.com/user-attachments/files/33232733/pruebas_no_supervisado.pdf)


 1.⁠ ⁠Descripción del proyecto

El proyecto consiste en el desarrollo de un sistema inteligente de rutas de transporte que integra técnicas de búsqueda y aprendizaje automático. Su propósito es encontrar rutas, estimar la duración de los viajes y analizar patrones en los datos de transporte.

El sistema integra un algoritmo de búsqueda A*, un modelo de aprendizaje supervisado para predecir la duración de los viajes y un componente de aprendizaje no supervisado basado en K-Means para agrupar viajes con características similares.

 2.⁠ ⁠Objetivo general

Desarrollar un sistema inteligente de rutas que integre técnicas de búsqueda, aprendizaje supervisado y aprendizaje no supervisado para encontrar rutas, predecir tiempos de recorrido e identificar agrupaciones de viajes según sus características.

 3.⁠ ⁠Tecnologías utilizadas

•⁠  ⁠Python: lenguaje de programación.
•⁠  ⁠pandas: manipulación y análisis de datos.
•⁠  ⁠scikit-learn: implementación de modelos de aprendizaje automático.
•⁠  ⁠K-Means: algoritmo de agrupamiento no supervisado.
•⁠  ⁠StandardScaler: estandarización de variables numéricas.
•⁠  ⁠Git y GitHub: control de versiones y alojamiento del código fuente.

 4.⁠ ⁠Funcionalidades del sistema

El menú principal cuenta con las siguientes opciones:

 1.⁠ ⁠Buscar la mejor ruta.
 2.⁠ ⁠Predecir la duración del viaje.
 3.⁠ ⁠Agrupar viajes mediante K-Means.
 4.⁠ ⁠Salir del sistema.

La tercera opción permite ejecutar el componente de aprendizaje no supervisado, analizar los grupos identificados y consultar las métricas obtenidas.

 5.⁠ ⁠Estructura del proyecto

sistema_rutas_ia_no_supervisado/
├── main.py
├── busqueda.py
├── conocimiento.py
├── reglas.py
├── modelo_supervisado.py
├── modelo_no_supervisado.py
├── pruebas_no_supervisado.py
└── datos/
    ├── dataset_transporte.csv
    ├── generar_dataset.py
    ├── dataset_agrupamiento.csv
    ├── generar_dataset_no_supervisado.py
    └── resultados_agrupamiento.csv

Nota: la estructura debe revisarse contra los archivos que realmente estén incluidos en el repositorio. Los documentos de descripción y pruebas se incorporarán como parte de la documentación final.

 6.⁠ ⁠Datos utilizados

Para el componente de aprendizaje no supervisado se utiliza el archivo datos/dataset_agrupamiento.csv, que contiene 150 registros sintéticos de viajes.

Las variables utilizadas son:

|Variable        |Descripción                       |
|----------------|----------------------------------|
|⁠ pasajeros ⁠     |Cantidad de pasajeros del viaje.  |
|⁠ distancia_km ⁠  |Distancia recorrida en kilómetros.|
|⁠ numero_paradas ⁠|Número de paradas del recorrido.  |
|⁠ duracion_min ⁠  |Duración del viaje en minutos.    |

Los datos son sintéticos y se utilizan con fines académicos. No corresponden a registros oficiales de un sistema real de transporte.

 7.⁠ ⁠Componente de aprendizaje no supervisado

El componente implementa el algoritmo K-Means, que permite agrupar registros según la similitud de sus características numéricas.

El procedimiento realizado es:

 1.⁠ ⁠Cargar el conjunto de datos.
 2.⁠ ⁠Verificar las columnas requeridas y la calidad básica de los registros.
 3.⁠ ⁠Estandarizar las variables mediante StandardScaler.
 4.⁠ ⁠Entrenar K-Means con tres grupos.
 5.⁠ ⁠Asignar un grupo a cada registro.
 6.⁠ ⁠Calcular las métricas del agrupamiento.
 7.⁠ ⁠Guardar los resultados en datos/resultados_agrupamiento.csv.

Resultados obtenidos

En la ejecución realizada se obtuvieron los siguientes resultados:

|Métrica               |Resultado|
|----------------------|--------:|
|Registros procesados  |150      |
|Grupos identificados  |3        |
|Inercia               |117.57   |
|Coeficiente de silueta|0.471    |

Los grupos presentan los siguientes promedios:

|Grupo|Pasajeros|Distancia promedio|Paradas promedio|Duración promedio|
|-----|--------:|-----------------:|---------------:|----------------:|
|0    |48.06    |3.03 km           |2.56            |14.62 min        |
|1    |252.98   |17.83 km          |11.86           |66.94 min        |
|2    |119.36   |8.57 km           |5.54            |32.08 min        |

Los resultados permiten distinguir perfiles de viajes cortos, intermedios y largos. El coeficiente de silueta de 0.471 indica una separación moderada entre los grupos, no una separación perfecta.

 8.⁠ ⁠Requisitos previos

Para ejecutar el proyecto se requiere:

•⁠  ⁠Python instalado.
•⁠  ⁠pip, el gestor de paquetes de Python.
•⁠  ⁠Las bibliotecas pandas y scikit-learn.

 9.⁠ ⁠Instalación

Clonar el repositorio:

git clone https://github.com/YariSoler/sistema-rutas-aprendizaje-no-supervisado.git

Ingresar a la carpeta del proyecto:

cd sistema-rutas-aprendizaje-no-supervisado

Instalar las dependencias:

python -m pip install pandas scikit-learn

10.⁠ ⁠Ejecución

Para iniciar el menú principal:

python main.py

Seleccionar la opción 3 para ejecutar el agrupamiento mediante K-Means.

También es posible ejecutar el modelo por separado:

python modelo_no_supervisado.py

Para ejecutar las pruebas del componente:

python pruebas_no_supervisado.py

11.⁠ ⁠Pruebas realizadas

Se implementó el archivo pruebas_no_supervisado.py para verificar:

•⁠  ⁠La existencia del conjunto de datos.
•⁠  ⁠La cantidad de registros.
•⁠  ⁠La presencia de las columnas requeridas.
•⁠  ⁠El procesamiento de los viajes.
•⁠  ⁠La identificación de tres grupos.
•⁠  ⁠La asignación de un grupo a cada registro.
•⁠  ⁠La validez de las métricas.
•⁠  ⁠La generación del archivo de resultados.

En la ejecución documentada, las ocho pruebas fueron aprobadas. El detalle se incluirá en el documento de pruebas del componente.

12.⁠ ⁠Limitaciones

•⁠  ⁠Los datos utilizados para el agrupamiento son sintéticos.
•⁠  ⁠El número de grupos se estableció en tres para esta implementación.
•⁠  ⁠Los resultados dependen de las variables seleccionadas y de las características de los datos.
•⁠  ⁠Las agrupaciones no representan conclusiones oficiales sobre el comportamiento del transporte real.

13.⁠ ⁠Conclusiones

La integración de K-Means amplía las funcionalidades del sistema inteligente de rutas al permitir explorar agrupaciones de viajes según sus características operativas.

El análisis de pasajeros, distancia, número de paradas y duración permite identificar perfiles de viajes y complementar las funcionalidades de búsqueda y predicción. Las métricas obtenidas proporcionan una primera evaluación del agrupamiento, teniendo en cuenta las limitaciones del conjunto de datos sintético.

Como trabajo futuro, se propone evaluar el modelo con datos reales y estudiar distintas configuraciones para determinar si es posible obtener agrupaciones mejor definidas.

Autoras: Naomy Restrepo
         Yaridiveth Soler

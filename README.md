# Guía de uso - Aprendizaje no supervisado

## Descripción general

Este proyecto desarrolla un análisis de rutas de transporte mediante un modelo de aprendizaje no supervisado, usando el algoritmo K-Means para agrupar automáticamente los datos en 3 segmentos. El script revisa la información contenida en `rutas_transporte.json`, analiza la relación entre `costo` y `distancia`, y genera un gráfico que permite identificar patrones de rutas con similar comportamiento.

La finalidad del proyecto es detectar grupos de rutas según sus características económicas y operativas, como por ejemplo:

- rutas cortas y económicas
- rutas medianas
- rutas largas y costosas

---

## Objetivo del archivo Python

El archivo principal de Python (`analisis_rutas.py`) debe:

1. Leer el archivo `rutas_transporte.json`
2. Cargar los datos en un DataFrame con pandas
3. Seleccionar las columnas relevantes para el análisis, generalmente `distancia_km` y `costo_pesos`
4. Normalizar los datos para evitar que una variable domine a otra
5. Aplicar el algoritmo K-Means con `n_clusters=3`
6. Generar un gráfico de dispersión mostrando la relación `costo_distancia`
7. Etiquetar cada registro según su grupo (Cluster 1, 2 o 3)
8. Guardar la visualización en un archivo gráfico

---

## ¿Qué hace el modelo?

El algoritmo de aprendizaje no supervisado utilizado es **K-Means**. Este método busca dividir los datos en un número fijo de grupos (en este caso 3), según la proximidad entre puntos.

### ¿Por qué K-Means?

Porque permite agrupar automáticamente observaciones sin necesidad de etiquetas previas. En este caso, cada ruta se considera como un punto con características como distancia y costo, y el algoritmo se encarga de formar grupos con comportamientos parecidos.

### Proceso del algoritmo

- Se define el número de clusters: `3`
- Se inicializan centroides aleatorios
- Se calcula la distancia de cada punto al centroide más cercano
- Se reasignan grupos según la menor distancia
- Se actualizan centroides
- Se repite el proceso hasta que los grupos se estabilizan

---


### Campos importantes

- `distancia_km`: longitud de la ruta
- `costo_pesos`: costo asociado a la ruta
- `tiempo_horas`: puede usarse como variable complementaria

---

## Relación costo vs distancia

La gráfica de relación `costo_distancia` es clave en este análisis porque ayuda a observar si:

- rutas largas tienden a ser más costosas
- hay rutas con costo elevado sin una distancia proporcionalmente alta
- existen grupos discretos de rutas con costos similares

Este tipo de visualización permite interpretar clusters formados por el algoritmo.

---

## Segmentación automática en 3 grupos

El modelo genera automáticamente tres grupos (clusters) a partir de los datos. Esto facilita la clasificación de rutas sin intervención manual.

### Ejemplo de interpretación de grupos

- Cluster 1: rutas cortas y económicas
- Cluster 2: rutas medianas
- Cluster 3: rutas largas y costosas

---

## Librerías instaladas y su importancia

Las librerías necesarias para este proyecto son:

- `pandas`: lectura y manipulación de datos en tablas
- `numpy`: operaciones matemáticas y manejo de arreglos
- `scikit-learn`: implementación del algoritmo K-Means
- `matplotlib`: generación de gráficos
- `seaborn`: visualización mejorada y más estética

### Importancia práctica

- `pandas` permite convertir el JSON en un DataFrame para facilitar el análisis.
- `numpy` ayuda en cálculos numéricos y preparación de datos.
- `scikit-learn` ejecuta la clustering automática con K-Means.
- `matplotlib` genera la gráfica de relación costo-distancia.
- `seaborn` mejora la estética del gráfico y facilita la interpretación visual.

---

## Requisitos del proyecto

Se recomienda mantener todos los archivos en una sola carpeta para facilitar la ejecución y evitar errores de rutas.

Estructura sugerida:

```text
carpeta_proyecto/
│
├── analisis_rutas.py
├── rutas_transporte.json
├── requirements.txt
├── grafico_clusters.png
└── README.md
```

Esto asegura que el script pueda leer el archivo JSON sin problemas y que la salida gráfica se genere en el mismo directorio.

---

## Instalación de dependencias

### Opción 1: instalar desde requirements.txt

```bash
pip install -r requirements.txt
```

### Opción 2: instalar librerías manualmente

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

---

## Ejecución del programa

Desde la carpeta donde se encuentran los archivos, ejecuta:

```bash
python analisis_rutas.py
```

### Resultado esperado

- Se cargan los datos del JSON
- Se realiza la segmentación automática en 3 grupos
- Se genera un gráfico con la relación `costo_distancia`
- Se muestran los resultados de clustering
- Se guarda una imagen del gráfico en la carpeta del proyecto

---


## Recomendaciones adicionales

- Verifica que el archivo `rutas_transporte.json` esté en la misma carpeta que el script
- Mantén los nombres de columnas exactos para evitar errores
- Si hay columnas con valores nulos, debes limpiarlas antes de ejecutar K-Means
- Puedes experimentar con más variables, como tiempo o número de paradas, para mejorar la segmentación

---

## Resultado esperado del proyecto

Al ejecutar el programa, se obtendrá lo siguiente:

- lectura de la información del JSON
- análisis no supervisado de rutas de transporte
- clasificación automática en 3 grupos
- gráfico visual de la relación costo-distancia
- identificación de patrones operativos y económicos

---

## Conclusión

Este proyecto demuestra cómo un modelo de aprendizaje no supervisado puede ayudar a segmentar rutas de transporte sin etiquetas previas. La combinación de `rutas_transporte.json`, K-Means y gráficos de costo-distancia permite detectar agrupaciones útiles para la toma de decisiones logísticas y de planificación.

---

## Autor

Edwar Vayron Andres

Actividad 3: Aprendizaje No Supervisado

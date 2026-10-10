import json
import math
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

RUTAS_ARCHIVO = "rutas_transporte.json"

# Ruta del archivo JSON
carpeta_programa = os.path.dirname(os.path.abspath(__file__))
archivo_json = os.path.join(carpeta_programa, RUTAS_ARCHIVO)

# Cargar datos
with open(archivo_json, 'r', encoding='utf-8') as f:
    datos = json.load(f)

# Listas para almacenar los datos

costos = []
distancias = []

 # Mostrar rutas y extraer datos
for r in datos:
    origen = r["origen"]
    destino = r["destino"]
    costo_val = r["costo"]
    distancia_val = r["distancia"]

    print(
        f"Ruta cargada: {origen} -> {destino}, "
        f"costo: {costo_val}, distancia: {distancia_val}"
    )

    distancias.append(distancia_val)
    costos.append(costo_val)


# Matriz de características
ANS = np.column_stack((distancias, costos))

# K-Means
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(ANS)
centroides = kmeans.cluster_centers_

# Visualización
plt.figure(figsize=(10, 6))

colores = ['red', 'blue', 'green']

for i in range(3):
    mascara = clusters == i
    plt.scatter(
        ANS[mascara, 0],
        ANS[mascara, 1],
        c=colores[i],
        s=100,
        alpha=0.6,
        edgecolors='black',
        label=f'Cluster {i + 1}'
    )

# Centroides
plt.scatter(
    centroides[:, 0],
    centroides[:, 1],
    c='yellow',
    marker='*',
    s=500,
    edgecolors='black',
    linewidth=2,
    label='Centroides'
)

plt.xlabel('Distancia', fontsize=12, fontweight='bold')
plt.ylabel('Costo', fontsize=12, fontweight='bold')
plt.title('K-Means: Clustering de Rutas', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
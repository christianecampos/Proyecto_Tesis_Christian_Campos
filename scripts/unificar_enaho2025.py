## ============================================================
## Script: unificar_enaho2025.py
## Autor: Christian Campos
## Proyecto: Tesis MAE - UBA
## Objetivo:
##     Unificar los cuatro trimestres de la ENAHO 2025 en una
##     única base anual, respetando la estructura del repositorio
##     y garantizando reproducibilidad académica.
##
##     Este script:
##       1. Lee los CSV trimestrales desde /datos/crudo/
##       2. Verifica consistencia de columnas
##       3. Concatena los cuatro trimestres
##       4. Exporta la base anual a /datos/procesado/
##
## ============================================================

### Importación de librerías necesarias
import pandas as pd
import os

### Definir paths relativos a las carpetas del repositorio
PATH_CRUDO = "../datos/crudo/"
PATH_PROCESADO = "../datos/procesado/"

### Listado explícito de archivos trimestrales
### Esto asegura control académico y evita lecturas accidentales
archivos_trimestrales = [
    "Enaho001-2025- 100-Trimestre 1.csv",
    "Enaho001-2025- 100- Trimestre 2.csv",
    "Enaho001-2025- 100- Trimestre 3.csv",
    "Enaho001-2025- 100- Trimestre 4.csv"

]

### Lista donde se almacenarán los DataFrames cargados
bases = []

## ============================================================
## LECTURA DE ARCHIVOS
## ============================================================

for archivo in archivos_trimestrales:
    ruta = os.path.join(PATH_CRUDO, archivo)
    
    ### Verificación académica: existencia del archivo
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"El archivo no existe: {ruta}")
    
    ### Lectura del CSV
    df = pd.read_csv(ruta, encoding="latin-1")
    
    ### Agregar columna indicadora del trimestre (útil para auditoría)
    df["trimestre"] = archivo
    
    bases.append(df)

## ============================================================
## VERIFICACIÓN DE CONSISTENCIA DE COLUMNAS
## ============================================================

### Extraemos las columnas del primer trimestre como referencia
columnas_ref = set(bases[0].columns)

for i, df in enumerate(bases[1:], start=2):
    columnas_actual = set(df.columns)
    if columnas_actual != columnas_ref:
        raise ValueError(f"Inconsistencia de columnas detectada en el trimestre {i}")

### Si llegamos aquí, las columnas son consistentes

## ============================================================
## CONCATENACIÓN DE LOS TRIMESTRES
## ============================================================

enaho2025_anual = pd.concat(bases, ignore_index=True)

## ============================================================
## EXPORTACIÓN DE LA BASE ANUAL
## ============================================================

### Crear carpeta procesado si no existe
os.makedirs(PATH_PROCESADO, exist_ok=True)

salida_csv = os.path.join(PATH_PROCESADO, "ENAHO2025_anual.csv")
enaho2025_anual.to_csv(salida_csv, index=False, encoding="latin-1")

print("Proceso completado con éxito.")
print(f"Base anual generada en: {salida_csv}")

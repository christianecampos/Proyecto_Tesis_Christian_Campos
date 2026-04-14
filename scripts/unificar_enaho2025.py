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
##       1. Lee los CSV trimestrales desde /data/raw/
##       2. Verifica consistencia de columnas
##       3. Concatena los cuatro trimestres
##       4. Exporta la base anual a /data/processed/
##
## ============================================================

import pandas as pd
import os

## ============================================================
## DEFINICIÓN DE RUTAS
## ============================================================

PATH_CRUDO = "../data/raw/"
PATH_PROCESADO = "../data/processed/"

## ============================================================
## ARCHIVOS TRIMESTRALES (RENOMBRADOS)
## ============================================================

archivos_trimestrales = [
    "ENAHO_2025_T1.csv",
    "ENAHO_2025_T2.csv",
    "ENAHO_2025_T3.csv",
    "ENAHO_2025_T4.csv"
]

bases = []

## ============================================================
## LECTURA DE ARCHIVOS
## ============================================================

print("=== INICIANDO UNIFICACIÓN DE ENAHO 2025 ===\n")

for archivo in archivos_trimestrales:
    ruta = os.path.join(PATH_CRUDO, archivo)

    print(f"Verificando archivo: {ruta}")

    if not os.path.exists(ruta):
        raise FileNotFoundError(f"El archivo no existe: {ruta}")

    df = pd.read_csv(ruta, encoding="latin-1")
    df["trimestre"] = archivo  # útil para auditoría

    print(f"  ✔ Cargado correctamente ({df.shape[0]} filas, {df.shape[1]} columnas)\n")

    bases.append(df)

## ============================================================
## VERIFICACIÓN DE CONSISTENCIA DE COLUMNAS
## ============================================================

columnas_ref = set(bases[0].columns)

for i, df in enumerate(bases[1:], start=2):
    columnas_actual = set(df.columns)
    if columnas_actual != columnas_ref:
        raise ValueError(f"Inconsistencia de columnas detectada en el trimestre {i}")

print("✔ Todas las columnas son consistentes entre trimestres.\n")

## ============================================================
## CONCATENACIÓN
## ============================================================

enaho2025_anual = pd.concat(bases, ignore_index=True)
print(f"✔ Base anual creada: {enaho2025_anual.shape[0]} filas totales.\n")

## ============================================================
## EXPORTACIÓN
## ============================================================

os.makedirs(PATH_PROCESADO, exist_ok=True)

salida_csv = os.path.join(PATH_PROCESADO, "ENAHO2025_anual.csv")
enaho2025_anual.to_csv(salida_csv, index=False, encoding="latin-1")

print("=== PROCESO COMPLETADO ===")
print(f"Base anual generada en: {salida_csv}")

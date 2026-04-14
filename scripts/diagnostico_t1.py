### ============================================================
### SCRIPT: diagnostico_t1.py
### PROYECTO: ENAHO 2025 — Curvas de Engel para bienes/servicios digitales
### AUTOR: Christian Campos
###
### DESCRIPCIÓN GENERAL:
###   Este script implementa el análisis completo del Trimestre 1
###   de la ENAHO 2025, con foco en las variables de bienes y
###   servicios digitales o modernos.
###
###   El objetivo principal es evaluar si el T1 contiene variables
###   monetarias necesarias para la construcción de curvas de Engel.
###   El análisis demuestra que el T1 solo releva variables de
###   tenencia (P114x), sin incluir los módulos de gasto (P1171–P1174).
###
###   Por lo tanto, el T1 es útil para describir acceso digital,
###   pero no aporta información monetaria continua, y resulta
###   insuficiente para estimar curvas de Engel.
###
###   Este script constituye el cierre formal del análisis del T1
###   y prepara el terreno para continuar con el Trimestre 2.
### ============================================================


### ============================================================
### BLOQUE 1 — IDENTIFICACIÓN DE VARIABLES PRESENTES EN T1
### ============================================================

variables_digitales_presentes = [
    var for var in [
        "P1141","P1142","P1143","P1144","P114B1","P114B2","P114B3",
        "P1171§11","P1171§12","P1171§13","P1171§14","P1171§17",
        "P1172§11","P1172§12","P1172§13","P1172§14","P1172§17",
        "P1173§11","P1173§12","P1173§13","P1173§14","P1173§17",
        "P1174§11","P1174§12","P1174§13","P1174§14","P1174§17"
    ]
    if var in df_test.columns
]

print("=== Variables de bienes/servicios digitales presentes en T1 ===")
print(variables_digitales_presentes)


### ============================================================
### BLOQUE 2 — ANÁLISIS DE CONSISTENCIA Y FORMATO
### ============================================================

print("\n=== Tipos de datos de variables digitales presentes ===")
print(df_test[variables_digitales_presentes].dtypes)

for col in variables_digitales_presentes:
    print(f"\n--- Distribución de valores: {col} ---")
    print(df_test[col].value_counts(dropna=False).head(10))

codigos_anomalos = [8, 9, 99]

print("\n=== Detección de códigos anómalos ===")
for col in variables_digitales_presentes:
    if df_test[col].dtype != "object":
        anom = df_test[df_test[col].isin(codigos_anomalos)]
        print(f"{col}: {len(anom)} casos con códigos anómalos")

if all(v in df_test.columns for v in ["P1144","P114B1","P114B2","P114B3"]):
    inconsistencias = df_test[
        (df_test["P1144"] == 0) &
        (
            (df_test["P114B1"] == 1) |
            (df_test["P114B2"] == 1) |
            (df_test["P114B3"] == 1)
        )
    ]
    print("\n=== Inconsistencias entre P1144 y variables derivadas ===")
    print("Cantidad de inconsistencias detectadas:", len(inconsistencias))


### ============================================================
### BLOQUE DE CIERRE DEL TRIMESTRE 1
### ============================================================

### SÍNTESIS METODOLÓGICA:
###
### 1. El Trimestre 1 solo contiene variables de TENENCIA:
###       P1141, P1142, P1143, P1144, P114B1, P114B2, P114B3
###
### 2. NO contiene variables de GASTO:
###       P1171, P1172, P1173, P1174
###
### 3. Esto significa que:
###       - T1 NO tiene montos monetarios.
###       - T1 NO permite construir curvas de Engel.
###       - T1 solo sirve para describir acceso digital.
###
### 4. Las variables presentes requieren limpieza:
###       - Todas vienen como 'object' por espacios en blanco.
###       - Hay miles de vacíos.
###       - No hay códigos anómalos numéricos.
###
### 5. Conclusión:
###       El T1 es útil para caracterizar acceso digital,
###       pero NO aporta información monetaria continua.
###       Por lo tanto, NO es operativo para estimar curvas de Engel.
###
### 6. Próximo paso:
###       Avanzar al Trimestre 2, donde se espera encontrar
###       los módulos de gasto necesarios para Engel.
###

print("\nCierre del análisis del Trimestre 1 completado. Listo para avanzar al Trimestre 2.")

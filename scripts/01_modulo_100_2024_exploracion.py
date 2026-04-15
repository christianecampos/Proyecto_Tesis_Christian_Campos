############################################################
######### PROYECTO: TESIS - CHRISTIAN CAMPOS
######### ARCHIVO: exploracion_enaho_2024.ipynb
######### OBJETIVO: Preparar entorno y cargar datos ENAHO
######### MODULO: 100 (Vivienda y Hogar)
############################################################

######### PASO 1: Clonar repositorio desde GitHub

!git clone https://github.com/christianecampos/Proyecto_Tesis_Christian_Campos.git

############################################################


######### PASO 2: Ingresar al directorio del proyecto

%cd Proyecto_Tesis_Christian_Campos

############################################################

######### PASO 3: Instalar herramienta para abrir archivos .rar

!apt-get install unrar -y

############################################################

######### PASO 4: Extraer archivo comprimido ENAHO 2024

!unrar x data/raw/Enaho01_2024_100.rar data/raw/

############################################################

######### VERIFICACION: Listar archivos extraídos

import os

archivos = os.listdir("data/raw")

print("Archivos disponibles en data/raw:")
print(archivos)

############################################################

############################################################
######### PASO 5: Leer encabezado del archivo (solo variables)
######### Esto NO carga datos completos (ahorra memoria RAM)
############################################################

import pandas as pd

######### Ruta del archivo CSV extraído

ruta_csv = "data/raw/Enaho01_2024_100.csv"

######### Leer SOLO encabezado

df = pd.read_csv(
    ruta_csv,
    sep=";",
    nrows=0
)

############################################################

######### RESULTADO: Número total de variables

print("Número total de variables:")

print(len(df.columns))

############################################################

######### RESULTADO: Lista completa de variables

print("Lista de variables:")

print(df.columns.tolist())

############################################################

############################################################
######### PASO 5: Leer encabezado del archivo (solo variables)
######### SOLUCIONANDO ERROR DE CODIFICACION
############################################################

import pandas as pd

######### Ruta del archivo CSV extraído

ruta_csv = "data/raw/Enaho01_2024_100.csv"

############################################################

######### Leer SOLO encabezado
######### encoding="latin1" evita error Unicode

df = pd.read_csv(
    ruta_csv,
    sep=";",
    encoding="latin1",
    nrows=0
)

############################################################

######### RESULTADO: Número total de variables

print("Número total de variables:")

print(len(df.columns))

############################################################

######### RESULTADO: Lista completa de variables

print("Lista de variables:")

print(df.columns.tolist())

############################################################

############################################################
######### PASO 5 (CORREGIDO): Leer encabezado correctamente
######### Detectando separador real (coma ",")
############################################################

import pandas as pd

######### Ruta del archivo CSV

ruta_csv = "data/raw/Enaho01_2024_100.csv"

############################################################

######### Leer encabezado correctamente

df = pd.read_csv(
    ruta_csv,
    sep=",",              ######### separador correcto
    encoding="latin1",    ######### evita error Unicode
    nrows=0
)

############################################################

######### RESULTADO: Número total de variables

print("Número total de variables:")

print(len(df.columns))

############################################################

######### RESULTADO: Lista completa de variables

print("Lista de variables:")

print(df.columns.tolist())

############################################################
🎯


############################################################
######### PASO 5 (CORREGIDO): Leer encabezado correctamente
######### Detectando separador real (coma ",")
############################################################

import pandas as pd

######### Ruta del archivo CSV

ruta_csv = "data/raw/Enaho01_2024_100.csv"

############################################################

######### Leer encabezado correctamente

df = pd.read_csv(
    ruta_csv,
    sep=",",              ######### separador correcto
    encoding="latin1",    ######### evita error Unicode
    nrows=0
)

############################################################

######### RESULTADO: Número total de variables

print("Número total de variables:")

print(len(df.columns))

############################################################

######### RESULTADO: Lista completa de variables

print("Lista de variables:")

print(df.columns.tolist())

############################################################

############################################################
######### PASO 7: Verificar presencia de variables TIC
############################################################

import pandas as pd

############################################################
######### Ruta del archivo

ruta_csv = "data/raw/Enaho01_2024_100.csv"

############################################################
######### Leer SOLO encabezado

df = pd.read_csv(
    ruta_csv,
    sep=",",
    encoding="latin1",
    nrows=0
)

############################################################
######### Lista de variables que queremos verificar

variables_objetivo = [

"P1141",
"P1142",
"P1143",
"P1144",
"P114B1",
"P114B2",
"P114B3",

"P1171$11",
"P1171$12",
"P1171$13",
"P1171$14",
"P1171$17",

"P1172$11",
"P1172$12",
"P1172$13",
"P1172$14",
"P1172$17",

"P1173$11",
"P1173$12",
"P1173$13",
"P1173$14",
"P1173$17",

"P1174$11",
"P1174$12",
"P1174$13",
"P1174$14",
"P1174$17"

]

############################################################
######### Verificar presencia

columnas = df.columns.tolist()

presentes = []
faltantes = []

for var in variables_objetivo:

    if var in columnas:
        presentes.append(var)

    else:
        faltantes.append(var)

############################################################
######### Mostrar resultados

print("=================================")
print("VARIABLES PRESENTES:")
print("=================================")

for v in presentes:
    print(v)

print("\n=================================")
print("VARIABLES FALTANTES:")
print("=================================")

for v in faltantes:
    print(v)

############################################################


############################################################
######### PASO 8: Inspección real de contenido
######### (mirar valores reales, no solo existencia)
############################################################

import pandas as pd

ruta_csv = "data/raw/Enaho01_2024_100.csv"

############################################################
######### Variables a inspeccionar

variables_objetivo = [

"P1141",
"P1142",
"P1143",
"P1144",

"P1171$11",
"P1171$12",
"P1171$13",
"P1171$14",
"P1171$17"

]

############################################################
######### Leer muestra razonable

df_sample = pd.read_csv(
    ruta_csv,
    sep=",",
    encoding="latin1",
    usecols=variables_objetivo,
    nrows=50000
)

############################################################
######### Inspección variable por variable

for var in variables_objetivo:

    print("=================================")
    print("VARIABLE:", var)
    print("=================================")

    print("Tipo:", df_sample[var].dtype)

    print("\nValores únicos (primeros 10):")
    print(df_sample[var].unique()[:10])

    print("\nResumen estadístico:")
    print(df_sample[var].describe())

    print("\nValores nulos:")
    print(df_sample[var].isnull().sum())

    print("\n\n")
    

############################################################
######### PASO 9: Buscar variables con montos reales
############################################################

import pandas as pd

ruta_csv = "data/raw/Enaho01_2024_100.csv"

############################################################

df = pd.read_csv(
    ruta_csv,
    sep=",",
    encoding="latin1",
    nrows=5000
)

############################################################
######### Buscar variables que parecen montos

posibles_montos = []

for col in df.columns:

    valores = df[col].astype(str).unique()

    # Si hay números mayores a 1, puede ser monto
    try:

        nums = pd.to_numeric(df[col], errors="coerce")

        if nums.max() > 5:
            posibles_montos.append(col)

    except:
        pass

############################################################

print("Variables que parecen montos:")

for v in posibles_montos:
    print(v)
    

############################################################
######### PASO 10: Inspección real de montos monetarios
############################################################

import pandas as pd

ruta_csv = "data/raw/Enaho01_2024_100.csv"

############################################################

variables_montos = [

"P1172$11",
"P1172$12",
"P1172$13",
"P1172$14",
"P1172$17"

]

############################################################

df_sample = pd.read_csv(
    ruta_csv,
    sep=",",
    encoding="latin1",
    usecols=variables_montos,
    nrows=50000
)

############################################################
######### Limpiar espacios vacíos

df_sample = df_sample.replace(" ", pd.NA)

############################################################
######### Convertir a numérico

for var in variables_montos:

    df_sample[var] = pd.to_numeric(
        df_sample[var],
        errors="coerce"
    )

############################################################
######### Mostrar resumen

for var in variables_montos:

    print("=================================")
    print("VARIABLE:", var)
    print("=================================")

    print(df_sample[var].describe())

    print("\nValores nulos:")
    print(df_sample[var].isnull().sum())

    print("\n\n")
    

############################################################
######### PASO 11: Porcentaje de ceros
############################################################

import pandas as pd

ruta_csv = "data/raw/Enaho01_2024_100.csv"

variables_clave = [

"P1172$12",
"P1172$13",
"P1172$14"

]

############################################################

df_sample = pd.read_csv(
    ruta_csv,
    sep=",",
    encoding="latin1",
    usecols=variables_clave
)

############################################################

df_sample = df_sample.replace(" ", pd.NA)

for var in variables_clave:

    df_sample[var] = pd.to_numeric(
        df_sample[var],
        errors="coerce"
    )

############################################################

total = len(df_sample)

for var in variables_clave:

    ceros = (df_sample[var] == 0).sum()
    positivos = (df_sample[var] > 0).sum()

    print("=================================")
    print("VARIABLE:", var)

    print("% CEROS:",
          round(ceros / total * 100, 2))

    print("% POSITIVOS:",
          round(positivos / total * 100, 2))

    print("\n")
    

############################################################
######### PASO 12: Construir gasto digital agregado
############################################################

import pandas as pd

ruta_csv = "data/raw/Enaho01_2024_100.csv"

variables_digital = [

"P1172$12",  # celular
"P1172$13",  # TV cable
"P1172$14"   # internet

]

############################################################

df = pd.read_csv(
    ruta_csv,
    sep=",",
    encoding="latin1",
    usecols=variables_digital
)

############################################################
######### Limpiar datos

df = df.replace(" ", pd.NA)

for var in variables_digital:

    df[var] = pd.to_numeric(
        df[var],
        errors="coerce"
    )

############################################################
######### Crear gasto digital total

df["GASTO_DIGITAL"] = df[
    variables_digital
].sum(axis=1, skipna=True)

############################################################
######### Resumen

print("=================================")
print("GASTO DIGITAL TOTAL")
print("=================================")

print(df["GASTO_DIGITAL"].describe())

print("\n% hogares con gasto positivo:")

positivos = (df["GASTO_DIGITAL"] > 0).sum()
total = len(df)

print(round(positivos / total * 100, 2))



df.columns[:50]



print(len(df.columns))

print(df.columns[:30])

print(df.columns[-30:])


Separaciòn de variables pagadas versus imputadas
print([
c for c in df.columns
if "1172" in c
])




print([
c for c in df.columns
if "1172" in c
][:50])

print([
c for c in df.columns
if "1173" in c
][:50])

print([
c for c in df.columns
if "1174" in c
][:50])



##### F I N   PRIMERA EXPLORACION MODULO 100

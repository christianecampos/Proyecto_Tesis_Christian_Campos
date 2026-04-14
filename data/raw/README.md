# Datos crudos (raw)

Esta carpeta contiene los archivos originales de la Encuesta Nacional de Hogares (ENAHO) correspondientes al año 2025, provistos en formato CSV y sin ningún tipo de modificación.

## Archivos incluidos

ENAHO_2025_T1.csv
ENAHO_2025_T2.csv
ENAHO_2025_T3.csv
ENAHO_2025_T4.csv

## Descripción

Cada archivo corresponde a un trimestre del año 2025 y contiene información socioeconómica recolectada por el INEI.  
Estos archivos se mantienen **íntegros y sin alteraciones**, respetando el principio de reproducibilidad académica.

## Uso en el proyecto

Estos datos serán utilizados por los scripts del directorio `guiones/` para:

1. Verificar consistencia entre trimestres  
2. Unificar los cuatro trimestres en una base anual  
3. Generar la base procesada en `datos/procesado/`  

Los archivos en esta carpeta **no deben modificarse manualmente*

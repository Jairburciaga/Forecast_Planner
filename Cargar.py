import pandas as pd
import os

def cargar(ruta_csv):
    logs = []
    
    # existe o no existe

    try:
        if not os.path.exists(ruta_csv):
            raise FileNotFoundError(f"❌ No se encontró el archivo: {ruta_csv}")
    except FileNotFoundError as e:
        logs.append(str(e))
        dataset = None
        return dataset, logs

    # Verificar la extensión, si es CSV o es Excel

    try:
        if ruta_csv.endswith('csv'):
            dataset = pd.read_csv(ruta_csv, sep=',')
        elif ruta_csv.endswith('xlsx'):
            dataset = pd.read_excel(ruta_csv)
        else:
            raise ValueError(f"❌ El formato del archivo {ruta_csv}\nDebes usar un archivo CSV ('.csv') o un archivo Excel ('.xlsx')\nNo se cargó el archivo")
    except ValueError as e:
        logs.append(str(e))
        dataset = None
        return dataset, logs
    

    # Verificar consistencia del dataset
    dataset.columns = [str(col).strip().lower() for col in dataset.columns]
    if dataset.shape[0] == 0:
        logs.append("⚠️ El dataset está Vacío. Se requiere, al menos, un registro además de los encabezados.")
    
    # Verificar si las columnas están bien definidas
    columnas_esperadas = ['sucursal', 'producto', 'año', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    columnas_actuales = [str(col).strip().lower() for col in dataset.columns]

    if set(columnas_esperadas) != set(columnas_actuales):
        logs.append(f"⚠️ Las columnas del dataset no estan en el formato requerido.\nDeberían estar como: {columnas_esperadas}")
    if len(columnas_actuales) != len(columnas_esperadas):
        logs.append(f"⚠️ El archivo tiene {len(columnas_actuales)}, Debería tener {len(columnas_esperadas)} columnas.")  
    for columna in columnas_esperadas:
        if columna not in columnas_actuales:
            logs.append(f"⚠️ La columna '{columna}' no se encuentra en el archivo.")
        
    # Mostrar errores

    if logs:
        dataset = None
        return dataset, logs
    
    # Si todo sale bien, cargar el dataset

    logs.append("✅ El Archivo se cargó correctamente")
    return dataset, logs
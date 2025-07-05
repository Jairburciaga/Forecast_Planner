from multiprocessing import Pool, cpu_count
import os
import pandas as pd
import numpy as np
from datetime import datetime
import math

logs = []

# Funcion principal que limpia el dataset
def limpiar_dataset(dataset):    
    # Verificar si tenemos dataset cargado
    try:
        if dataset is None:
            raise ValueError("❌ Primero debes cargar un archivo válido.")
    except ValueError as e:
        logs.append(str(e))
        return None, logs
    
    # Activar el paso 1
    try:
        dataset['sucursal'] = dataset['sucursal'].astype(str)
        dataset.fillna(0, inplace=True)
        df_filtrado, df_descartados = clasificar_grupos(dataset)
    except Exception as e:
        logs.append(f"Error en el paso 1 del proceso de limpieza: {str(e)}")
        return None, logs
    
    # Activar paso 2
    try: 
        dataset_sin_nulos = rellenar_nulos_por_fila(df_filtrado)
    except Exception as e:
        logs.append(f"Error en el paso 2 del proceso de limpieza: {str(e)}")
        return None, logs
    # Activar paso 3
    try:
        df_listo = corregir_outliers_estacionales(dataset_sin_nulos)
        dataset_sin_nulos = None
        df_filtrado = None     #liberamos memoria de los pasos anteriores
        logs.append("✅ El archivo se ha procesado correctamente y esta listo")
    except Exception as e:
        logs.append(f"Error en el paso 3 del proceso de limpieza: {str(e)}")
        return None, logs
    return df_listo, logs
    
        ### PASO 1, SEPARAR PRODUCTOS SIN VENTAS DE LOS QUE TIENEN VENTAS ###

# suma las columnas de la lista de columnas meses, retorna true si la suma es 0
def es_grupo_vacío(grupo_df):
    columnas_meses = [str(i) for i in range(1, 13)]
    return grupo_df[columnas_meses].sum().sum() == 0

# clasifica los grupos dividiendo entre los que tienen ventas y los que no
def clasificar_grupos(dataset):
    columnas_meses = [str(i) for i in range(1, 13)]
    dataset['sucursal'] = dataset['sucursal'].astype('category')
    dataset['producto'] = dataset['producto'].astype('category')

    # Agrupar por sucursal + producto
    grupos = [grupo for _, grupo in dataset.groupby(['sucursal', 'producto'])]

    with Pool(processes=min(6, cpu_count())) as pool:
        resultados = pool.map(es_grupo_vacío, grupos)

    # Separar grupos según el resultado
    grupos_con_ventas = [grupos[i] for i in range(len(grupos)) if not resultados[i]]
    grupos_vacíos = [grupos[i][['sucursal', 'producto']].iloc[0] for i in range(len(grupos)) if resultados[i]]

    # Combinar los útiles en un solo DataFrame
    df_filtrado = pd.concat(grupos_con_ventas, ignore_index=True)
    df_descartados = pd.DataFrame(grupos_vacíos).drop_duplicates()

    return df_filtrado, df_descartados

        ### PASO 2 manejar los valores faltantes ###
    
def rellenar_nulos_por_fila(dataset):
    mes_actual = datetime.now().month
    año_actual = datetime.now().year
    columnas_meses = [str(i) for i in range(1, 13)]

    # Iterar por cada fila
    for i, fila in dataset.iterrows():
        año = fila['año']
    # si es el año actual solo trabajar los meses validos, si no date compa
        if año < año_actual:
            columnas_validas = columnas_meses  
        elif año == año_actual:
            columnas_validas = [str(m) for m in range(1, mes_actual + 1)] 
        else:
            continue  # Ignorar años futuros

        # Calcular promedio solo con datos válidos
        promedio = fila[columnas_validas].mean()

        # Rellenar los NaN en los meses válidos
        for col in columnas_validas:
            if pd.isnull(dataset.at[i, col]):
                dataset.at[i, col] = promedio
    
    df_completo = dataset.copy()
    return df_completo

        ### PASO 3, CORREGIR OUTLIERS ###

def corregir_outliers_estacionales(dataset, n_periodos=3, n_std=2.0):
    mes_actual = datetime.now().month
    año_actual = datetime.now().year
    columnas_meses = [str(i) for i in range(1, 13)]

    # Generar bloques estacionales dinámicamente
    meses_por_bloque = math.ceil(12 / n_periodos)
    bloques_estacionales = {}

    for i in range(n_periodos):
        inicio = i * meses_por_bloque + 1
        fin = min(inicio + meses_por_bloque - 1, 12)
        bloques_estacionales[f"bloque_{i+1}"] = [str(m) for m in range(inicio, fin + 1)]

    def corregir_grupo(grupo):
        grupo = grupo.copy()

        for bloque, columnas in bloques_estacionales.items():
            columnas_validas = []
            for col in columnas:
                col_int = int(col)
                for año in grupo['año'].unique():
                    if año < año_actual or (año == año_actual and col_int <= mes_actual):
                        columnas_validas.append(col)

            columnas_validas = list(set(columnas_validas))
            if not columnas_validas:
                continue

            bloque_vals = grupo[columnas_validas]
            media = bloque_vals.mean().mean()
            std = bloque_vals.stack().std()

            lim_sup = media + n_std * std
            lim_inf = media - n_std * std

            grupo[columnas_validas] = bloque_vals.applymap(
                lambda x: lim_sup if x > lim_sup else lim_inf if x < lim_inf else x
            )

        return grupo

    df_listo = dataset.groupby(['sucursal', 'producto']).apply(corregir_grupo).reset_index(drop=True)
    return df_listo


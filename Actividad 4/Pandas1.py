# %%

import pandas as pd
import numpy as np

# %%
url = "https://raw.githubusercontent.com/plotly/datasets/master/supermarket_Sales.csv"

data = pd.read_csv(url)

data = data.rename(columns={
    'Tax 5%': 'Tax',
    'Cost of goods sold': 'Cogs',
    'Gross margin percentage': 'Gross margin pct',
    'Customer stratification rating': 'Rating'
})

data.columns = (
    data.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
)
# %% 1. Dimensiones del DataFrame

print(data.shape)

# %% 2. Columnas, tipos y primeras filas

print(data.columns) # Nombres de las columnas
print(data.dtypes) # tipo de dato de cada variable
data.head(3) #muestra las 3 primeras filas 

# %% Seleccionar datos
#Ejercicio 3. Seleccionar varias columnas

resultado = data[['product_line', 'quantity', 'total']]

resultado.head()


# %% 4. ¿Series o DataFrame?

print(type(data['total'])) # Series
print(type(data[['total']])) # Dataframe


# %% 5. loc e iloc sobre la misma celda

print(data.loc[7, 'product_line'])
print(data.iloc[7, 5])

# %% 6. Una sola condición

mascara = data['quantity'] > 8
resultado = data[mascara]
print(resultado.shape[0])


# %% 7. Dos condiciones al mismo tiempo

mascara = (data['branch'] == 'C') & (data['total'] > 300)
resultado = data[mascara]
print(resultado.shape)

# %% 8. Corregir un filtro por categorías

# incorrecto
#data['product_line'] == 'Food and beverages' or 'Fashion accessories'

mascara = data['product_line'].isin([
    'Food and beverages',
    'Fashion accessories'
])

print(data[mascara].shape[0])

# %% 9. Rango de valores y columnas elegidas

mascara = (
    data['branch'].isin(['A', 'C'])
) & (
    data['total'].between(200, 500)
)

resultado = data.loc[
    mascara,
    ['branch', 'product_line', 'quantity', 'total']
]

resultado.head()
# %% 10. Valor de cada unidad vendida

data['valor_unitario'] = data['total'] / data['quantity']
print(data['valor_unitario'].head(3).round(2))

# %% 11. Clasificar cada venta

data['tipo_compra'] = np.where(
    data['quantity'] >= 6,
    'volumen',
    'menor'
)

print(data['tipo_compra'].value_counts())

# %% 12. ¿Cuánto ingreso genera cada sucursal?

resumen = (
    data
    .groupby('branch')['total']
    .sum()
)

print(resumen.round(2))

# %% 13. ¿Cuántas facturas registra cada método de pago?

resumen = (data.groupby('payment')['invoice_id'].count())
print(resumen)

# %% 14. Varias métricas por método de pago

resumen = (
    data
    .groupby('payment')
    .agg(
        facturas=('invoice_id', 'size'),
        unidades=('quantity', 'sum'),
        ingreso=('total', 'sum'),
    )
    .reset_index()
)

print(resumen.round(2))


# %% 15. Agregar la zona de cada sucursal

sucursales = pd.DataFrame({
    'branch': ['A', 'B', 'C'],
    'zona': ['Centro', 'Norte', 'Sur']
})

resultado = data.merge(
    sucursales,
    on='branch',
    how='left'
)

print(resultado.shape)

resultado[['branch', 'city', 'zona', 'total']].head()

# %% 16 Ejercicio integrador

#1. Filtrar Member
#2. Agrupar por branch
#3. Contar facturas
#4. Sumar ingreso
#5. Calcular ticket promedio
#6. Ordenar

# Filtrar
miembros = data[
    data['customer_type'] == 'Member'
].copy()

# 2. Agrupar por sucursal

resumen = (
    miembros
    .groupby('branch')
    .agg(
        facturas=('invoice_id', 'size'),
        ingreso=('total', 'sum')
    )
    .reset_index()
)

# %% 3. Calcular ticket promedio

# Según el propio ejercicio:

#ticket promedio = ingreso / número de facturas

resumen['ticket_promedio'] = (
    resumen['ingreso'] / resumen['facturas']
)

# %% 4. Ordenar de mayor a menor ingreso

resumen = resumen.sort_values(
    'ingreso',
    ascending=False
)

# 5. Mostrar el resultado
print(resumen.round(2))

# Entre los clientes de tipo Member, la sucursal C presenta el mayor
# ingreso total. Su ticket promedio es aproximadamente USD 336,58 
# por factura, superior al de las sucursales B y A.

# %%

# Dimensiones
#data.shape

# Primeras filas data.head()

# Una columna → Series
# data['total']

# Varias columnas → DataFrame
# data[['branch', 'total']]

# Selección por etiquetas
# data.loc[filas, columnas]

# Selección por posiciones
# data.iloc[filas, columnas]

# Una condición
# data[data['quantity'] > 8]

# Varias condiciones
#data[(data['branch'] == 'C') & (data['total'] > 300)]

# Varias categorías
#data['branch'].isin(['A', 'C'])

# Rango
#data['total'].between(200, 500)

# Nueva columna
#data['nueva'] = data['total'] / data['quantity']

# Condición para nueva columna
#np.where(condicion, 'valor1', 'valor2')

# Agrupar y sumar
#data.groupby('branch')['total'].sum()

# Varias métricas
#data.groupby('payment').agg(...)

# Unir dos tablas
#data.merge(otra_tabla, on='clave', how='left')

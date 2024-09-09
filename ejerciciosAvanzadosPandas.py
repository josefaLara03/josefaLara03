import pandas as pd

# DataFrames de ejemplo
df_prices = pd.DataFrame({
    'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06']),
    'ID': ['X', 'Y', 'X', 'Z', 'Y', 'Z'],
    'Price': [50, 60, 55, 70, 65, 75],
    'Moneda': ['USD', 'USD', 'EUR', 'USD', 'EUR', 'USD']
})

df_weights = pd.DataFrame({
    'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-05']),
    'ID': ['X', 'Y', 'Z', 'Y'],
    'Weight': [0.5, 0.3, 0.2, 0.4],
    'Status': ['Activo', 'Inactivo', 'Activo', 'Activo']
})
print(df_prices)

# Merge df_prices with df_weights on 'Date' and 'ID'
merged_df = pd.merge(df_prices, df_weights, on=['Date', 'ID'], how='left')

# Fill missing weights with the most recent available weight
merged_df['Weight'] = merged_df.groupby('ID')['Weight'].ffill()

# Calculate the weighted average price
merged_df['Weighted_Price'] = merged_df['Price'] * merged_df['Weight']
weighted_avg_price = merged_df.groupby('ID').apply(lambda x: x['Weighted_Price'].sum() / x['Weight'].sum())

#print(weighted_avg_price)

# Factor de conversión
conversion_factor = 0.9

# Convertir 'Price' a EUR para los 'ID' con 'Status' 'Activo' en df_weights
active_ids = df_weights[df_weights['Status'] == 'Activo']['ID'].unique()
df_prices['Converted_Price'] = df_prices.apply(
    lambda row: row['Price'] * conversion_factor if row['ID'] in active_ids and row['Moneda'] == 'USD' else row['Price'],
    axis=1
)

#print(df_prices)

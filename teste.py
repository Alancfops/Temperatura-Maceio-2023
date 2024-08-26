import pandas as pd

# Carregar o arquivo CSV
dados = pd.read_csv('TPG.csv', sep=';', header=0)

# Verificar as primeiras linhas e colunas
print(dados.head())
print(dados.columns)
print(dados.dtypes)

# Renomear colunas para simplificar
dados.columns = [
    'Data', 'Hora UTC', 'Precipitacao_Total', 'Pressao_Atmosferica_Nivel_Estacao',
    'Pressao_Atmosferica_Max', 'Pressao_Atmosferica_Min', 'Radiacao_Global',
    'Temperatura_Do_Ar_Bulbo_Seco', 'Temperatura_Ponto_Orvalho', 'Temperatura_Maxima',
    'Temperatura_Minima', 'Temperatura_Orvalho_Max', 'Temperatura_Orvalho_Min',
    'Umidade_Rel_Max', 'Umidade_Rel_Min', 'Umidade_Relativa_Do_Ar',
    'Vento_Direcao_Horaria', 'Vento_Rajada_Maxima', 'Vento_Velocidade_Horaria'
]

# Converter colunas para numérico e preencher valores NaN
dados['Temperatura_Maxima'] = pd.to_numeric(dados['Temperatura_Maxima'], errors='coerce')
dados['Temperatura_Minima'] = pd.to_numeric(dados['Temperatura_Minima'], errors='coerce')
dados['Temperatura_Maxima'].fillna(dados['Temperatura_Maxima'].mean(), inplace=True)
dados['Temperatura_Minima'].fillna(dados['Temperatura_Minima'].mean(), inplace=True)

# Calcular estatísticas
media_maxima = dados['Temperatura_Maxima'].mean()
mediana_maxima = dados['Temperatura_Maxima'].median()
moda_maxima = dados['Temperatura_Maxima'].mode().iloc[0] if not dados['Temperatura_Maxima'].mode().empty else None

media_minima = dados['Temperatura_Minima'].mean()
mediana_minima = dados['Temperatura_Minima'].median()
moda_minima = dados['Temperatura_Minima'].mode().iloc[0] if not dados['Temperatura_Minima'].mode().empty else None

# Imprimir resultados
print(f"Média da temperatura máxima: {media_maxima}")
print(f"Mediana da temperatura máxima: {mediana_maxima}")
print(f"Moda da temperatura máxima: {moda_maxima}")

print(f"Média da temperatura mínima: {media_minima}")
print(f"Mediana da temperatura mínima: {mediana_minima}")
print(f"Moda da temperatura mínima: {moda_minima}")

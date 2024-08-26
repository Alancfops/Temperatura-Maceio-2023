import pandas as pd

# Carregar o arquivo CSV, ajustando o cabeçalho
dados = pd.read_csv('TPG.csv', sep=';', header=3)

# Exibir as primeiras linhas e colunas para verificar
print(dados.head())
print(dados.columns)

# Converter colunas para numérico e tratar valores faltantes
dados['TEMPERATURA MAXIMA'] = pd.to_numeric(dados['TEMPERATURA MAXIMA'], errors='coerce')
dados['TEMPERATURA MINIMA'] = pd.to_numeric(dados['TEMPERATURA MINIMA'], errors='coerce')

# Preencher valores NaN com a média das colunas
dados['TEMPERATURA MAXIMA'] = dados['TEMPERATURA MAXIMA'].fillna(dados['TEMPERATURA MAXIMA'].mean())
dados['TEMPERATURA MINIMA'] = dados['TEMPERATURA MINIMA'].fillna(dados['TEMPERATURA MINIMA'].mean())

# Calcular estatísticas
media_maxima = dados['TEMPERATURA MAXIMA'].mean()
mediana_maxima = dados['TEMPERATURA MAXIMA'].median()
moda_maxima = dados['TEMPERATURA MAXIMA'].mode().iloc[0] if not dados['TEMPERATURA MAXIMA'].mode().empty else None

media_minima = dados['TEMPERATURA MINIMA'].mean()
mediana_minima = dados['TEMPERATURA MINIMA'].median()
moda_minima = dados['TEMPERATURA MINIMA'].mode().iloc[0] if not dados['TEMPERATURA MINIMA'].mode().empty else None

# Imprimir resultados
print(f"Média da temperatura máxima: {media_maxima}")
print(f"Mediana da temperatura máxima: {mediana_maxima}")
print(f"Moda da temperatura máxima: {moda_maxima}")

print(f"Média da temperatura mínima: {media_minima}")
print(f"Mediana da temperatura mínima: {mediana_minima}")
print(f"Moda da temperatura mínima: {moda_minima}")
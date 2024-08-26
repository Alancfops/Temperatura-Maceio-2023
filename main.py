import pandas as pd

# Carregar o arquivo CSV
dados = pd.read_csv('TPG.csv', sep=';', header=0)

# Converter colunas para numérico e preencher valores NaN com 0
dados['TEMPERATURA MAXIMA'] = pd.to_numeric(dados['TEMPERATURA MAXIMA'], errors='coerce').fillna(0)
dados['TEMPERATURA MINIMA'] = pd.to_numeric(dados['TEMPERATURA MINIMA'], errors='coerce').fillna(0)

# Converter colunas para listas
lista_maxima = dados['TEMPERATURA MAXIMA'].tolist()
lista_minima = dados['TEMPERATURA MINIMA'].tolist()

# Calcular estatísticas diretamente com pandas
media_maxima = pd.Series(lista_maxima).mean()
mediana_maxima = pd.Series(lista_maxima).median()
moda_maxima = pd.Series(lista_maxima).mode().iloc[0] if not pd.Series(lista_maxima).mode().empty else None

media_minima = pd.Series(lista_minima).mean()
mediana_minima = pd.Series(lista_minima).median()
moda_minima = pd.Series(lista_minima).mode().iloc[0] if not pd.Series(lista_minima).mode().empty else None

# Imprimir resultados
print(f"Média da temperatura máxima: {media_maxima}")
print(f"Mediana da temperatura máxima: {mediana_maxima}")
print(f"Moda da temperatura máxima: {moda_maxima}")

print(f"Média da temperatura mínima: {media_minima}")
print(f"Mediana da temperatura mínima: {mediana_minima}")
print(f"Moda da temperatura mínima: {moda_minima}")

import pandas as pd


caminho_csv = 'TPG.csv'


dados = pd.read_csv(caminho_csv, sep=';', header=4)

dados.columns = [
    'Data', 'Hora UTC', 'Precipitacao Total', 'Pressao Atmosferica Estacao',
    'Pressao Atmosferica Maxima', 'Pressao Atmosferica Minima', 'Radiacao Global',
    'Temperatura Ar', 'Temperatura Ponto Orvalho', 'Temperatura Maxima',
    'Temperatura Minima', 'Temperatura Orvalho Maxima', 'Temperatura Orvalho Minima',
    'Umidade Relativa Maxima', 'Umidade Relativa Minima', 'Umidade Relativa',
    'Vento Direcao', 'Vento Rajada Maxima', 'Vento Velocidade Horaria'
]

dados['Data'] = pd.to_datetime(dados['Data'], dayfirst=True, format='%d/%m/%Y', errors='coerce')

dados['Temperatura Maxima'] = pd.to_numeric(dados['Temperatura Maxima'].str.replace(',', '.'), errors='coerce')
dados['Temperatura Minima'] = pd.to_numeric(dados['Temperatura Minima'].str.replace(',', '.'), errors='coerce')

dados['Temperatura Maxima'] = dados['Temperatura Maxima'].fillna(0)
dados['Temperatura Minima'] = dados['Temperatura Minima'].fillna(0)

dados['Mês'] = dados['Data'].dt.month

resultados_maxima = dados.groupby('Mês')['Temperatura Maxima'].agg(
    Média='mean', Mediana='median', Moda=lambda x: x.mode()[0] if not x.mode().empty else None
).reset_index()

resultados_minima = dados.groupby('Mês')['Temperatura Minima'].agg(
    Média='mean', Mediana='median', Moda=lambda x: x.mode()[0] if not x.mode().empty else None
).reset_index()

resultados_maxima = resultados_maxima.round({'Média': 1, 'Mediana': 1, 'Moda': 1})
resultados_minima = resultados_minima.round({'Média': 1, 'Mediana': 1, 'Moda': 1})

print("Estatísticas da Temperatura Máxima por Mês:")
print(resultados_maxima)

print("\nEstatísticas da Temperatura Mínima por Mês:")
print(resultados_minima)
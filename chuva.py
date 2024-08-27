
import pandas as pd
import matplotlib.pyplot as plt

caminho_csv = 'TPG.csv'

dados = pd.read_csv(caminho_csv, sep=';', header=4)

dados.columns = [
    'Data', 'Hora UTC', 'PRECIPITACAO TOTAL', 'Pressao Atmosferica Estacao',
    'Pressao Atmosferica Maxima', 'Pressao Atmosferica Minima', 'Radiacao Global',
    'Temperatura Ar', 'Temperatura Ponto Orvalho', 'Temperatura Maxima',
    'Temperatura Minima', 'Temperatura Orvalho Maxima', 'Temperatura Orvalho Minima',
    'Umidade Relativa Maxima', 'Umidade Relativa Minima', 'Umidade Relativa',
    'Vento Direcao', 'Vento Rajada Maxima', 'Vento Velocidade Horaria'
]

dados = dados.dropna(how='all')

dados['Data'] = pd.to_datetime(dados['Data'], errors='coerce')

if dados['Data'].isnull().all():
    print("Erro na conversão de datas. Verifique o formato da coluna 'Data'.")
else:
    dados['PRECIPITACAO TOTAL'] = pd.to_numeric(dados['PRECIPITACAO TOTAL'], errors='coerce')

    dados['PRECIPITACAO TOTAL'] = dados['PRECIPITACAO TOTAL'].fillna(0)

    dados['Mês'] = dados['Data'].dt.month

    precipitacao_mensal = dados.groupby('Mês')['PRECIPITACAO TOTAL'].sum()

    nomes_dos_meses = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ]

    if precipitacao_mensal.index.dtype == float:
        precipitacao_mensal.index = precipitacao_mensal.index.astype(int)

    precipitacao_mensal.index = precipitacao_mensal.index.map(lambda x: nomes_dos_meses[x-1])

    if precipitacao_mensal.sum() == 0:
        print("Nenhum dado de precipitação para plotagem.")
    else:
        plt.figure(figsize=(14, 7))
        precipitacao_mensal.plot(kind='bar')
        plt.xlabel('Mês')
        plt.ylabel('Precipitação Total (mm)')
        plt.title('Precipitação Total Mensal em Maceió')
        plt.xticks(rotation=360) 
        plt.grid(True, axis='y')
        plt.tight_layout()
        plt.show()
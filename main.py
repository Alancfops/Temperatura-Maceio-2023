import pandas as pd
import matplotlib as plt


df =  pd.read_csv('TPG.CSV')
media = df['temperatura'].mean()


import pandas as pd
import numpy as np
from procura_arquivos import procura

matrizes_diagonais = procura("matriz_diagonal_real*.csv", "../arquivos_csv/")
lista_de_nos = pd.read_csv("../arquivos_csv/lista_de_nos.csv", index_col=0)
lista_de_nos = lista_de_nos.reset_index(drop=True)
lista_de_nos_numpy = lista_de_nos.to_numpy()
modos_criticos = pd.DataFrame(columns=["local","magnitude"])

for matriz in matrizes_diagonais:
    matriz_diagonal = pd.read_csv("../arquivos_csv/{}".format(matriz), index_col=0)
    matriz_diagonal_inversa = np.linalg.inv(matriz_diagonal)
    matriz_diagonal_inversa_df = pd.DataFrame(matriz_diagonal_inversa)
    matriz_diagonal_inversa_df.index = lista_de_nos
    matriz_diagonal_inversa_df.columns = lista_de_nos
    matriz_diagonal_inversa_df.to_csv("../arquivos_csv/inversa_{}".format(matriz))
    valores_diagonais = np.linalg.diagonal(matriz_diagonal_inversa)
    valores_minimos = pd.DataFrame(valores_diagonais, index=lista_de_nos, columns=["autovalores"])
    valores_minimos.to_csv("../arquivos_csv/valores_minimos_{}".format(matriz))
    valores_minimos_ordenados = valores_minimos.sort_values(by=["autovalores"])
    valores_minimos_ordenados.to_csv("../arquivos_csv/valores_minimos_ordenados_{}".format(matriz))
    modo_critico = valores_minimos_ordenados.iloc[0,0]
    indice_modo_critico = valores_minimos_ordenados[valores_minimos_ordenados["autovalores"] == modo_critico].index[0]
    #no_modo_critico = lista_de_nos_numpy[indice_modo_critico]
    modos_criticos.loc[matriz] = indice_modo_critico, modo_critico

modos_criticos.to_csv('../arquivos_csv/modos_criticos.csv')
print("Modos críticos encontrados e salvos no arquivo 'modos_criticos.csv'")
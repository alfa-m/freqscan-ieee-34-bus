import pandas as pd
import numpy as np
from procura_arquivos import procura

lista_de_matrizes_y = procura("imaginario_y*.csv", '../arquivos_csv/')

for matriz_y in lista_de_matrizes_y:
    caminho = "../arquivos_csv/{}".format(matriz_y)
    matriz_y_df = pd.read_csv(caminho, index_col=0)
    autovalores_matriz_y, autovetores_matriz_y = np.linalg.eig(matriz_y_df)
    matriz_y_diagonal = np.diag(autovalores_matriz_y)
    matriz_y_diagonal_df = pd.DataFrame(matriz_y_diagonal)
    matriz_y_diagonal_df.to_csv("../arquivos_csv/matriz_diagonal_{}".format(matriz_y))
    autovetores_matriz_y_df = pd.DataFrame(autovetores_matriz_y)
    autovetores_matriz_y_df.to_csv("../arquivos_csv/autovetores_{}".format(matriz_y))

print("Matrizes Y imaginário decompostas diagonalmente e matrizes de autovetores obtidas")

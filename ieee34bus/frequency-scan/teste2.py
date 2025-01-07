import pandas as pd

matriz_y = pd.read_csv("y_teste_2.csv", index_col=0)

lista_de_nos = pd.read_csv("lista_de_nos.csv", index_col=0)

matriz_y_real = []
matriz_y_imaginario = []
colunas = lista_de_nos.values
matriz_y_real_completa = pd.DataFrame(index=colunas, columns=colunas)
matriz_y_imaginario_completa = pd.DataFrame(index=colunas, columns=colunas)
k = 0
m = 0

for i in range(len(lista_de_nos)):
    for j in range(m,m+(2*len(lista_de_nos))):
        if j % 2 == 0:
            matriz_y_real.append(matriz_y.iloc[j,0])
        else:
            matriz_y_imaginario.append(matriz_y.iloc[j,0])

    for l in range(len(lista_de_nos)):
        matriz_y_real_completa.iloc[i,l] = matriz_y_real[k]
        matriz_y_imaginario_completa.iloc[i,l] = matriz_y_imaginario[k]
        k = k + 1

    m = m + (l * 2) + 2

matriz_y_real_pd = pd.DataFrame(matriz_y_real)
matriz_y_real_pd.to_csv("matriz_y_real.csv")
matriz_y_imaginario_pd = pd.DataFrame(matriz_y_imaginario)
matriz_y_imaginario_pd.to_csv("matriz_y_imaginario.csv")

matriz_y_real_completa_pd = pd.DataFrame(matriz_y_real_completa)
matriz_y_real_completa_pd.to_csv("matriz_y_real_completa.csv")
matriz_y_imaginario_completa_pd = pd.DataFrame(matriz_y_imaginario_completa)
matriz_y_imaginario_completa_pd.to_csv("matriz_y_imaginario_completa.csv")


import pandas as pd
from procura_arquivos import procura

arquivos_y = procura("y_*.csv", "../arquivos_csv/")

lista_de_nos = pd.read_csv("../arquivos_csv/lista_de_nos.csv", index_col=0)
colunas = lista_de_nos.values

vetorYreal = []
vetorYimaginario = []

matrizYreal = pd.DataFrame(index=colunas, columns=colunas)
matrizYimaginario = pd.DataFrame(index=colunas, columns=colunas)

for arquivo in arquivos_y:
    arquivo_df = pd.read_csv("../arquivos_csv/{}".format(arquivo), index_col=0)

    k = 0

    for i in range(len(lista_de_nos)):
        for j in range((2 * k), (2 * k) + (2 * len(lista_de_nos))):
            if j % 2 == 0:
                vetorYreal.append(arquivo_df.iloc[j, 0])
            else:
                vetorYimaginario.append(arquivo_df.iloc[j, 0])

        for l in range(len(lista_de_nos)):
            matrizYreal.iloc[i, l] = vetorYreal[k]
            matrizYimaginario.iloc[i, l] = vetorYimaginario[k]
            k = k + 1

    matrizYreal.to_csv("../arquivos_csv/real_{}".format(arquivo))
    matrizYimaginario.to_csv("../arquivos_csv/imaginario_{}".format(arquivo))

print("Fim da criação das matrizes Y real e Y imaginário")

import os, fnmatch

def procura(padrao, caminho):
    resultado = []
    for raiz, diretorios, arquivos in os.walk(caminho):
        for nome in arquivos:
            if fnmatch.fnmatch(nome, padrao):
                resultado.append(nome)
    return resultado
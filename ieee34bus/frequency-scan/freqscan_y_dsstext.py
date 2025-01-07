import py_dss_interface
import numpy as np
import os
import pathlib

# Inicializa o objeto DSS
dss = py_dss_interface.DSS(r"C:\Program Files\OpenDSS")

# Adiciona o path e compila o arquivo .dss
script_path = os.path.dirname(os.path.abspath(__file__))
dss_file = pathlib.Path(script_path).joinpath("ieee34Mod1.dss")
dss.text("Compile [{}]".format(dss_file))
dss.dssinterface.allow_forms = 0

# Adiciona dados de coordenadas das barras
dss.text("Buscoords BusCoords.dat")

# Cria variaveis contendo o nome das linhas, barras e nós
nomesLinhas = dss.lines.names
nomesBarras = dss.circuit.buses_names
nomesNos = dss.circuit.nodes_names

# Realiza a solução do fluxo de potência para obter os valores de magnitude e fase das tensões e correntes
dss.solution.solve()

# Remove demais fontes harmonicas
dss.text("Spectrum.DefaultLoad.NumHarm=1")

# Adiciona um monitor em cada linha
for i in range(len(nomesLinhas)):
    linha = nomesLinhas[i]
    dss.text("New Monitor.MonitorLine{} Line.{} 1 mode=0".format(linha, linha))

# Salva nomes dos monitores
nomesMonitores = dss.monitors.names

# Define o espectro de frequências a serem analisadas
harmonicos = np.arange(1,51,2).tolist()
dss.text("New spectrum.espectroharmonico numharm={} csvfile=espectro_harmonico.csv".format(str(len(harmonicos))))

#  Adiciona a fonte de corrente harmônica de sequência positiva
node = nomesNos[0]
barra = node.split(".")
barra = barra[0]
scansource = "Isource.scansource{}".format(node)
dss.text("New {} bus1={} amps=1 spectrum=espectroharmonico".format(scansource,node))

dss.solution.solve()

# Seleciona o modo de solução harmonic
dss.text("Set mode=harmonic")

# Realiza a solução harmônica iterada
for h in range(len(harmonicos)):
    dss.text("Set harmonic={}".format(harmonicos[h]))
    dss.solution.solve()
    indice = "frequencia_" + str(round(harmonicos[h]*60,1))
    dss.monitors.reset_all()

    print(" Frequência " + str(round(harmonicos[h]*60,1)))

    dss.text("Export Y")
    os.rename("ieee34-1_EXP_Y.csv", "y_dsstext_frequencia_{}.csv".format(str(round(harmonicos[h]*60,1))))

print("Análise harmônica finalizada")

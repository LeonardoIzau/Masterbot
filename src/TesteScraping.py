from ParsehubController import ParsehubController
from DatabaseController import DatabaseController
import numpy as np

# Insira sua api_key e projectToken do Parsehub
api_key = ''
projectToken = ''

# Insira os dados de seu banco MySQL
host = 'localhost'
user = 'root'
password = 'root'
database = 'Boadica'

pc = ParsehubController(api_key, projectToken)
dc = DatabaseController(host, user, password, database)

tipoPecas = ['cpu', 'gpu', 'motherboard']
cpu = tipoPecas[0]

slices = list(np.arange(0, 1125, 125))

dc.carregarPecas(cpu)
for i in range(0, len(slices)):
    if slices[i] < slices[-1]:
        runToken = pc.executaConsultaPrecos(cpu, slices[i], slices[i+1])
        resultRun= pc.getConsultaPrecos(runToken)
        dc.atualizaPrecos(resultRun, cpu)
    else: break

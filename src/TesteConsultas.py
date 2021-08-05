from DatabaseController import DatabaseController

host = 'localhost'
user = 'root'
password = 'root'
database = 'Boadica'

dc = DatabaseController(host, user, password, database)
tipoPecas = ['cpu', 'gpu', 'motherboard']
tp = tipoPecas[0]

results1 = dc.consultaPrecos(1, tp, 'Intel', 'Celeron G1610')
results2 = dc.consultaPrecos(2, tp)

for row in results1:
    print("Resultado da busca pela peca do tipo '%s': [%s]" % (tp, row))

print("\nLista de pecas do tipo %s com preco nao nulo:" % tp)

for row in results2:
    print(row)
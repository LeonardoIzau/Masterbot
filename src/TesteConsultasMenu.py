from DatabaseController import DatabaseController

host = 'localhost'
user = 'root'
password = 'root'
database = 'Boadica'

dc = DatabaseController(host, user, password, database)

opcao = -1
print("Bem vindo ao sistema Masterbot!")
while opcao != 0:
    print("\nEscolha uma opcao!")
    print("\n0 - Sair")
    print("1 - Consultar o preco de uma peca (gpu, cpu ou motherboard)")
    print("2 - Consultar os precos de todas as pecas da tabela desejada (gpu, cpu ou motherboard)")
    opcao = int(input())
    if opcao == 1:
        tipoPeca = input("\nDigite o tipo da peca (gpu, cpu ou motherboard):")
        marca, modelo = input("Digite o nome da peca (marca + modelo):").split(" ", 1)
        results = dc.consultaPrecos(1, tipoPeca, marca, modelo)
        for row in results:
            print("\nResultado da busca pela peca do tipo '%s': [%s]" % (tipoPeca, row))
    elif opcao == 2:
        tipoPeca = input("\nDigite o tipo da peca (gpu, cpu ou motherboard):")
        results = dc.consultaPrecos(2, tipoPeca)
        print("\nLista de pecas do tipo %s com preco nao nulo:" % tipoPeca)
        for row in results:
            print(row)
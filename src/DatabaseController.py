import pymysql
import csv
import json

class DatabaseController:
   def __init__(self, host, user, password, database):
      self.host = host
      self.user = user
      self.password = password
      self.database = database

   def carregarPecas(self, tipoPeca):
      # Abrir conexão com banco de dados MySQL
      db = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.database)

      # Preparar um objeto cursor com o método cursor()
      cursor = db.cursor()

      # Define a consulta SQL para extrair a chave de busca de cada peça
      sql = """SELECT CONCAT(brand, " ", model) AS pecas FROM %s;""" % tipoPeca

      # Inicializa a tabela de resultados (valor padrão caso não encontre resultados
      results = []
      try:
         print("Extracao de dados da tabela %s iniciada!\n" % tipoPeca)
         # Executa o comando sql
         cursor.execute(sql)
         # Insere todas as linhas em uma lista de listas.
         results = cursor.fetchall()
      except:
         print("Erro: incapaz de extrair dados da tabela %s" % tipoPeca)

      # Nome do arquivo csv de saída da consulta
      nomeArq = 'consulta_%s.csv' % (tipoPeca)
      with open(nomeArq,'w', newline='') as out:
         csv_out=csv.writer(out)
         # Escreve o cabeçalho da tabela no csv
         csv_out.writerow(['pecas'])
         # Escreve as linhas da consulta no csv
         for row in results:
            csv_out.writerow(row)

      # desconecta do servidor MySQL
      db.close()
      print("Extração de dados da tabela %s feita com sucesso!\n" % tipoPeca)

   def atualizaPrecos(self, tabPrecos, tipoPeca):
      # Abrir conexão com banco de dados MySQL
      db = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.database)

      # Preparar um objeto cursor com o método cursor()
      cursor = db.cursor()

      print("Atualizacao de precos da tabela %s foi iniciada!\n" % tipoPeca)

      # Carrega a string json em memória como um dicionário
      tabPrecos_dict = json.loads(tabPrecos)
      # Reorganiza os dados do dicionário
      tabPrecos_dict = tabPrecos_dict['lista_de_precos']
      for i in tabPrecos_dict:
         try:
            # Extrai o nome de cada peça
            nomePeca = i['nomePeca']
            # Separa a nome da peça em marca e modelo
            marca, modelo = nomePeca.split(" ", 1)
            # Extrai o preço de cada peça
            preco = i['preco']
            # Converte o preco em ponto flutuante
            preco_f = float((preco.replace('R$ ', '')).replace(',', '.'))
            # Define o comando sql para atualizar os precos
            sql = """UPDATE %s SET price='%.2f' WHERE brand='%s' AND model='%s'""" % (tipoPeca, preco_f, marca, modelo)
            print("Peca atualizada na tabela %s -> marca = %s, modelo = %s, preco = %s" % (tipoPeca, marca, modelo, preco))
            try:
               # Executa o comando sql
               cursor.execute(sql)
               # Confirma as mudanças no banco de dados
               db.commit()
            except:
               # Rollback no caso de qualquer erro
               db.rollback()
         except KeyError:
            print("A peça nao tem preco!")
      print("Atualizacao de precos da tabela %s concluida!\n" % tipoPeca)
      db.close()

   def consultaPrecos(self, opcao, tipoPeca, marca="", modelo=""):
      # Open database connection
      db = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.database)

      # prepare a cursor object using cursor() method
      cursor = db.cursor()

      sql = """"""

      if opcao == 1:
         # Create table as per requirement
         sql = """SELECT brand, model, price FROM %s WHERE brand='%s' AND model='%s';""" % (tipoPeca, marca, modelo)
      elif opcao == 2:
         sql = """SELECT brand, model, price FROM %s WHERE price IS NOT NULL;""" % (tipoPeca)
      try:
         print("Consulta de precos na tabela %s iniciada\n" % tipoPeca)
         # Execute the SQL command
         cursor.execute(sql)
         # Fetch all the rows in a list of lists.
         results = cursor.fetchall()
      except:
         print("Erro: incapaz de extrair dados da tabela %s" % tipoPeca)
         results = None
      print("Consulta de precos da tabela %s concluida!\n" % tipoPeca)
      db.close()
      return results


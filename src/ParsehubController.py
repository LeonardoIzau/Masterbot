import csv
import json
import requests
import time

class ParsehubController:

  def __init__(self, api_key, projectToken):
    self.api_key = api_key
    self.projectToken = projectToken

  def executaConsultaPrecos(self, tipoPeca, sliceStartPos, sliceEndPos):
    print("Extracao dos precos de %s no Parsehub iniciada!\n" % tipoPeca)
    csvFileName = 'consulta_%s.csv' % tipoPeca
    query = {'pecas':[]}
    with open(csvFileName, newline='') as csvFile:
      reader = csv.DictReader(csvFile)
      for row in (r for i, r in enumerate(reader) if sliceStartPos <= i < sliceEndPos):
        query['pecas'].append(row['pecas'])
      queryString = json.dumps(query)

    params = {
      "api_key": "%s" % self.api_key,
      "start_url": "https://www.boadica.com.br",
      "start_template": "main_template",
      "start_value_override": "%s" % queryString,
      "send_email": "0"
    }

    run_address = 'https://www.parsehub.com/api/v2/projects/%s/run' % self.projectToken
    r = requests.post(run_address, data=params)
    r_json = json.loads(r.text)
    print("Extracao dos precos de %s no Parsehub encerrada!\n" % tipoPeca)
    return r_json["run_token"]	

  def getConsultaPrecos(self, runToken):
    print("Extracao de dados da run no Parsehub iniciada!\n")
    params = {
      "api_key": "%s" % self.api_key
    }
    run_address = 'https://www.parsehub.com/api/v2/runs/%s' % runToken
    r = requests.get(run_address, params=params)
    r_json = json.loads(r.text)
    while r_json["data_ready"] == 0:
      print("\nEsperando o termino da run...")
      time.sleep(120)
      r = requests.get(run_address, params=params)
      r_json = json.loads(r.text)
    print("\nRun extraida!")

    params = {
      "api_key": "%s" % self.api_key,
      "format": "json"
    }

    run_address = 'https://www.parsehub.com/api/v2/runs/%s/data' % runToken
    r = requests.get(run_address, params=params)
    print("Extracao de dados da run no Parsehub encerrada!\n")
    return r.text



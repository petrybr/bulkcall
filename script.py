#!/usr/bin/env python2.7
import requests
from requests.auth import HTTPBasicAuth
import getpass
import csv


login = raw_input("Login: ")
passwd = getpass.getpass('Senha: ')

print "Abrindo arquivo"
with open('endpoints.csv', 'r') as arquivo:
    print "Processando arquivo"
    endpoints = csv.DictReader(arquivo)

print "Atuando nos endpoints"
for endpoint in endpoints:
    print "Conectando em: " + endpoint["Nome"]
    with requests.Session() as s:
        r = s.get('http://' + endpoint["ip"] + '/getxml?location=/Status/SystemUnit/State', auth=(login,passwd))
    print r.text

print "Completed!"

# verificar lista dos endpoints
# perguntar por username e senha
# conectar em cada um dos endpoints
## Abrir sessao
##  http://<ip-address>/xmlapi/session/begin
# verificar se ja nao esta em uma chamada
## se ja estiver, ver o que fazer, alertar? desconectar?
## se nao estiver, fazer a ligacao
# fechar sessao com endpoint
# ter ctz q a sessao foi encerrada com sucesso p evitar problemas

# calcular o tempo total para conectar todos endpoints
#!/usr/bin/env python2.7
import requests
from requests.auth import HTTPBasicAuth
import getpass

ENDPOINT_IP = "192.168.250.66"

login = raw_input("Login: ")
passwd = getpass.getpass('Senha: ')
print "Entrando no with"

with requests.Session() as s:
    r = s.get('http://192.168.250.66/getxml?location=/Status/Call/Status', auth=(login,passwd))
    print r.text

print "Sai do with"
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
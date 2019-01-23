#!/usr/bin/env python2.7
import requests
from requests.auth import HTTPBasicAuth
import getpass
import csv
import xmltodict


login = raw_input("Login: ")
passwd = getpass.getpass('Password: ')
destination = raw_input("Address to call: ")

with open('endpoints.csv', 'r') as arquivo:
    endpoints = csv.DictReader(arquivo)
    for endpoint in endpoints:
        with requests.Session() as s:
            r = s.get('http://' + endpoint["ip"] + '/getxml?location=/Status/SystemUnit/State', auth=(login,passwd))
            xml = xmltodict.parse(r.text)
            actives = xml['Status']['SystemUnit']['State']['NumberOfActiveCalls']
            progress = xml['Status']['SystemUnit']['State']['NumberOfInProgressCalls']
            suspended = xml['Status']['SystemUnit']['State']['NumberOfSuspendedCalls']
            total = int(actives) + int(progress) + int(suspended)
            #print "Chamadas ativas: " + actives
            #print "Chamadas em progresso: " + progress
            #print "Chamadas suspensas: " + suspended
            #print "Total de chamadas: " + str(total)
            if total == 0:
                print "Ok, placing a new call"
                mydict = { 'Command': { 'Dial': { 'Number': destination, }}}
                dicttoxml = xmltodict.unparse(mydict)
                headers = {'Content-Type': 'text/xml'}
                s.post('http://' + endpoint["ip"] + '/putxml', data=dicttoxml, headers=headers,auth=(login,passwd))

            else:
                print "Endpoint already in a call: " + endpoint["Nome"]


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
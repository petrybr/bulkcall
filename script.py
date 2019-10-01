#!/usr/bin/env python2.7

#
## https://github.com/petrybr/bulkcall
#

import requests
from requests.auth import HTTPBasicAuth
import getpass
import csv
import xmltodict
import time
inicio = time.time()
login = raw_input("Login: ")
passwd = getpass.getpass('Password: ')
destination = raw_input("Address to call: ")

with open('endpoints.csv', 'r') as arquivo:
    endpoints = csv.DictReader(arquivo)
    for endpoint in endpoints:
        if endpoint["Connect"] == "yes":
            with requests.Session() as s:
                try:
                    r = s.get('http://' + endpoint["ip"] + '/getxml?location=/Status/SystemUnit/State', auth=(login,passwd))
                except requests.ConnectionError as e:
                    print "Connection Error - " + endpoint["Name"]
                    continue
                except requests.Timeout as e:
                    print "Timeout Error - " + endpoint["Name"]
                    continue
                except requests.RequestException as e:
                    print "General Error - " + endpoint["Name"]
                    continue
                xml = xmltodict.parse(r.text)
                actives = xml['Status']['SystemUnit']['State']['NumberOfActiveCalls']
                progress = xml['Status']['SystemUnit']['State']['NumberOfInProgressCalls']
                suspended = xml['Status']['SystemUnit']['State']['NumberOfSuspendedCalls']
                total = int(actives) + int(progress) + int(suspended)
                if total == 0:
                    print "Dialing to " + destination + " from " + endpoint["Nome"]
                    mydictdial = { 'Command': { 'Dial': { 'Number': destination, }}}
                    mydictmute = { 'Command': { 'Audio': { 'Microphones': { 'Mute': { '@command': 'True'}}}}}
                    dicttoxmldial = xmltodict.unparse(mydictdial)
                    dicttoxmlmute = xmltodict.unparse(mydictmute)
                    headers = {'Content-Type': 'text/xml'}
                    s.post('http://' + endpoint["ip"] + '/putxml', data=dicttoxmldial, headers=headers,auth=(login,passwd))
                    s.post('http://' + endpoint["ip"] + '/putxml', data=dicttoxmlmute, headers=headers,auth=(login,passwd))
                else:
                    print "Endpoint " + endpoint["Name"] + " already in a call"
        else:
                print "Endpoint " + endpoint["Name"] + " is configured to not join this call in endpoints.csv"
fim = time.time()
tempo = fim - inicio
print "Completed in " + str(tempo).split(".")[0] + " seconds!"
raw_input("Press enter to exit")


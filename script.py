#!/usr/bin/env python2.7

################################################################################
#   Copyright (C) 2019 - José Paulo de Oliveira Petry <petrybr AT gmail.com>   #
#                                                                              #
#   This program is free software: you can redistribute it and/or modify       #
#   it under the terms of the GNU General Public License as published by       #
#   the Free Software Foundation, either version 3 of the License, or          #
#   (at your option) any later version.                                        #
#                                                                              #
#   This program is distributed in the hope that it will be useful,            #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of             #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              #
#   GNU General Public License for more details.                               #
#                                                                              #
#   You should have received a copy of the GNU General Public License          #
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.     #
################################################################################
#
## https://github.com/petrybr/bulkcall
#

import requests
from requests.auth import HTTPBasicAuth
import getpass
import csv
import xmltodict
import time
login = raw_input("Login: ")
passwd = getpass.getpass('Password: ')
destination = raw_input("Address to call: ")
inicio = time.time()

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
                    print "Dialing to " + destination + " from " + endpoint["Name"]
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


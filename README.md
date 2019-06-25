# bulkcall

Make 1 or more Cisco Endpoints dial to one specific destination Address

Based on: https://www.cisco.com/c/dam/en/us/td/docs/telepresence/endpoint/ce96/collaboration-endpoint-software-api-reference-guide-ce96.pdf

Uses Python 2.7

Libraries: requests, xmltodict, getpass, csv, time

file endpoints.csv with the Endpoint name, ip address to access, and if it is to connect or not
endpoints.csv headers: Nome,ip,conectar

Nome = name of endpoint
ip = ip address of endpoint
conectar = "sim" if it is to connect to this endpoint


Need to have an user at the endpoints with proper roles

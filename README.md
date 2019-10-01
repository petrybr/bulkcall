# bulkcall

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/petrybr/bulkcall)

Make 1 or more Cisco Endpoints dial to one specific destination Address

Based on: https://www.cisco.com/c/dam/en/us/td/docs/telepresence/endpoint/ce96/collaboration-endpoint-software-api-reference-guide-ce96.pdf

Uses Python 2.7

Libraries: requests, xmltodict, getpass, csv, time

configure the endpoints in file endpoints.csv with the Endpoint name, ip address to access, and if it is to connect or not
endpoints.csv headers: Name,ip,connect 

Name = name of endpoint (for reference only)

ip = ip address of endpoint

connect = "yes" if it is to connect to this endpoint


Need to have an user at the endpoints with proper roles. same user/password in all endpoints

when run the script, it will ask the user/pwd to connect to and the "Dial to" address. The it will read the endpoints.csv file searching for all endpoints that are marked with "connect = yes", then it will login to each end point, check if it is in a call. If it is in a call it will logout from the endpoint and connect to the next. If it is not in  a call it will send a command to the endpoint to dial to the destination address, and will mute the microphone. After this command is sent, it will logout and connect to the next endpoint.

In the end it will show how long it took.

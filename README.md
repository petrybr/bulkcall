# bulkcall - Remotely start calls in a bulk
<!---
[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/petrybr/bulkcall)
-->
## Use Case

Imagine you have 37 Cisco Webex Room Kits over different cities and you need them to call to a Webex Personal Room for a meeting, and you need to start these calls remotely without an user doing this manually on site.

So you would need to enter the web interface of each one of these 37 endpoints, navigate to the call menu, and start a call to your destination. It can take a few minutes, or more, depending on how many endpoints you have.

## Solution

I created this script to automatically  connect to each of a list of endpoints and send a command for them to call to the meeting. For my situation, I reduced from 10 minutes to manually make the calls to ~2 minutes running the script.

## How it Works?

When you run the script it will ask the destination SIP URI you want to call and the username and password of the endpoints. 

Then, for each of the endpoints in the list (endpoints.csv), the script will send a REST API GET to check if the endpoint is in a call or not. 

  - If it **is in a call**, it will log this information in the console and dismiss this endpoint, going to the next in the list. 
  - If it **is not in a call**, it will send a REST API POST Call command so the endpoint will dial to the destination SIP URI Address.
  Then it will send a REST API POST command to mute the microphone (so the endpoints join the call muted, avoiding disturbing if the meeting is already running). Then it will log the information that the endpoint is dialing to the meeting and will go to the next endpoint in the list.

## Requirements

* Python 2.7
* Libraries: requests, xmltodict, getpass, csv, time
* An user created in each of the endpoints, with the USER ROLE. The username and password MUST be the same in all endpoints. (Check endpoint [admin guide](https://www.cisco.com/c/en/us/support/collaboration-endpoints/spark-room-kit-series/products-maintenance-guides-list.html) to see how to do that)
* Network connection from the computer where is the script running to the endpoints
* A file (in the same folder of the script) called "endpoints.csv" with the following information: endpoint name, ip address, connect flag

## How to use it

1. Clone this repo

```
  git clone https://github.com/petrybr/bulkcall.git
```

2. Install the requirements

```
  pip install -r requirements.txt
```

3. Edit the endpoints.csv file with your information:

  - **Name**: A name to identify the endpoint the script is connecting
  
  - **ip**: The IP address of the endpoints. It's the IP address the script will connect.
  
  - **connect**: the options here are "yes" or "no". It's just to say to the script if it is to start a call in this endpoint (yes) or no (no). Just to avoid needing to remove the entry if for some reason today you don't need that endpoint to connect to the call (but you may need it tomorrow).
  
4. Run it!

```
  python script.py
```

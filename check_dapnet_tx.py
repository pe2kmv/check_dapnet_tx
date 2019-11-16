import sys
import requests
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t','--transmitter',help='add transmitter call sign')
args = parser.parse_args()

if args.transmitter == None:
	print("No TX specified")
	sys.exit(1)

hampagerurl = "http://www.hampager.de:8080/transmitters/" + args.transmitter
try:
	response = requests.get(hampagerurl,timeout=5)
except:
	print("DAPNET UNKNOWN")
	sys.exit(3)

if response.status_code == 200:
	json_response = json.loads(response.content)
	txstate = json_response['status']
	if txstate =="ONLINE":
		print("DAPNET OK")
		sys.exit(0)
	else:
		print("DAPNET CRITICAL")
		sys.exit(2)

else:
	print("Transmitter unknown")
	sys.exit(3)



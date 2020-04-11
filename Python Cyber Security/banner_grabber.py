import sys
import requests
import socket
import json
 
  
#check command line arguments
  
if len(sys.argv) < 2:
print("Usage: " + sys.argv[0] + " <url>")
sys.exit(1)
  
 
#get request to the provided hostname
req = requests.get("https://"+sys.argv[1])
print("\n"+ str(req.headers))
  
#hostname to ip
gethostby = socket.gethostbyname(sys.argv[1])
  
print("\n The Ip address is " + gethostby)
 
 
#ipinfo.io  for ip location look up
#request to api 
req_two = requests.get("http://ipinfo.io/"+gethostby + "/json")
resp = json.loads(req_two.text)
  
print("Location: " + resp['loc'])
print("Region: " + resp['region'])
print("City: " + resp['city'])
print("Country: " + resp['country'])

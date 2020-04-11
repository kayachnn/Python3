# this program scans 21, 22, 80, 139, 443, 8080

import nmap
import sys
import socket

# check command line arguments
if len(sys.argv) < 2 :
 	print("Usage: " + str(sys.argv[0] + " target")
 	sys.exit(1)

target = socket.gethostbyname(sys.argv[1])

ports = [21, 22, 80, 139, 443, 8080]

scan_v = nmap.PortScanner()

print("\nScanning" + target + "for ports 21, 22, 80, 139, 443, 8080 \n")

for port in ports:
 	portscan = scan_v.scan(target, str(port))
        print("Port" +  str(port) + " is " + portscan['scan'][target]['tcp'][port]['state'])


print("\nHost", target, " is ", portscan['scan'][target]['status']['state'])

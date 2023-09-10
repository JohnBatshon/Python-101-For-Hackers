#!/bin/python3

# Port Scanner

# Import

import sys
import socket
from datetime import datetime

# Define Target
# Translate hostname to IPv4 Address.

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
	
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 ./port-scanner.py <IP Address>")

# Add a pretty banner
print("-" * 50)
print("Scanning target: "+target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
	for port in range(20,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"Port {port} is open")
		s.close()

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved.")
	
except socket.error:
	print("Could not connect to the server.")
	sys.exit()


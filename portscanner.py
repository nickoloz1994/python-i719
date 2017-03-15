import threading
import time
import socket
import sys
from datetime import datetime
import thread

# list for active ports
ports = []

# thread class
class myThread(threading.Thread):
	def __init__(self, rmip, p1, p2):
		threading.Thread.__init__(self)
		self.rmip = rmip
		self.p1 = p1
		self.p2 = p2
	def run(self):
		scantcp(self.rmip, self.p1, self.p2)

# method which is called by each thread for scanning port range
def scantcp(rmip, p1, p2):
	for port in range(p1, p2):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(2)
		result = sock.connect_ex((rmip,port))

		if result == 0:
			ports.append(port)
			sock.close()

# user input
rmip = raw_input("Enter IP address to scan: ")
stp = int(raw_input("Enter starting port number: "))
endp = int(raw_input("Enter last port number: "))

print "Scanning ports for IP address: {0}".format(rmip)

# time when scanning started
t1 = datetime.now()

totalPorts = endp - stp
portsPerThread = 30
if totalPorts%portsPerThread != 0:
	totalThread = totalPorts/portsPerThread + 1
else:
	totalThread = totalPorts/portsPerThread

if totalThread > 300:
	portsPerThread = totalPorts/300
	if totalPorts%portsPerThread != 0:
		totalThread = totalPorts/portsPerThread + 1
	else:
		totalThread = totalPorts/portsPerThread

# list for active threads
threads = []

# create threads and define port ranges for each
for i in range(totalThread):
	p2 = stp + portsPerThread
	thread = myThread(rmip, stp, p2)
	thread.start()
	threads.append(thread)
	stp = p2

# terminate all threads
for t in threads:
	t.join()

# sort and display active ports
ports.sort()
for p in ports:
	print "Port Open: --> {0}".format(p)

# display elapsed time
t2 = datetime.now()
totalTime = t2 - t1
print "Scanning complete in {0}".format(totalTime)

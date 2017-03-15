import collections
import os
import socket, subprocess,sys
import threading
from datetime import datetime

# input the network address and split into octets
network = raw_input("Enter the Network Address: ")
octets = network.split('.')
p = '.'
netaddr = octets[0] + p + octets[1] + p + octets[2] + p

start = int(raw_input("Enter the starting host address: "))
end = int(raw_input("Enter the last host address: "))
end = end + 1
myDict = collections.OrderedDict()

ping = "ping -c 1 "

t1 = datetime.now()

# thread class which initializes itself
class myThread (threading.Thread):
	def __init__(self,start_addr,end):
		threading.Thread.__init__(self)
		self.start_addr = start_addr
		self.end = end
	def run(self):
		run1(self.start_addr,self.end)

# this function will be used by each thread to check
# their ip address ranges respectively
def run1(start,end):
	for ip in xrange(start,end):
		address = netaddr + str(ip)
		command = ping + address
		response = os.system(command)
		if response == 0:
			myDict[ip] = address			

# total number of ip addresses to be scanned
totalIP = end - start
# total number of ip addresses that will be
# scanned by each thread
totalNumber = 10
# total number of threads
totalThread = totalIP/totalNumber
if totalIP%totalNumber != 0:
	totalThread += 1
# list of threads
threads = []

# start all threads with appropriate ip ranges
# and put each thread in the list of threads

try:
	for i in xrange(totalThread):
		end1 = start + totalNumber
		if end1 > end:
			end1 = end
		thread = myThread(start,end1)
		thread.start()
		threads.append(thread)
		start = end1
except:
	print "Error: Unable to start thread"

print "\t"
print "Number of active threads: {0}".format(threading.activeCount())

# terminate all threads
for t in threads:
	t.join()

print "Exiting main thread"
dic = collections.OrderedDict(sorted(myDict.items()))

print "\t"

# print out host addresses that are active
for key in dic:
	print "Host {0} is Live".format(dic[key])

t2 = datetime.now()
totalTime = t2 - t1
print "\t"
print "Scanning completed in {0}".format(totalTime)

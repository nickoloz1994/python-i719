import socket
import sys

def scanport(remip, portnum):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1)

	result = sock.connect_ex((remip,portnum))

	if result == 0:
		print "Port Open:--->{0}".format(portnum)
		return 1
	else:
		print "Port {0} is closed".format(portnum)
		return 0
		sys.exit()
	sock.close()

def main():
	option = raw_input("Press D for Domain Name or I for IP address: ")

	if option == 'D' or option == 'd':
		rmhost = raw_input("Enter the Domain Name: ")
		rmip = socket.gethostbyname(rmhost)
	elif option == 'I' or option == 'i':
		rmip = raw_input("Enter the remote host IP address to scan: ")
	else:
		print "Wrong input"
		sys.exit()
	
	port = int(raw_input("Enter the port number to scan: "))

	try:
		scanport(rmip,port)
	except KeyboardInterrupt:
		print "Scanning stopped"
		sys.exit()
	except socket.error:
		print "Couldn't connect to host"
		sys.exit()

	print "Scanning Complete"	

if __name__ == '__main__':
	main()
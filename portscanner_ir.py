#!/usr/bin/python2.7
#submitted by itsmeroy2012
#A simple port scanner that requires only python to scan for open ports.
#usage:- ip-provided an ip address range for example:- '-H 172.29.43.*'  (scans from ip addresses 172.29.43.1 to 172.29.43.250)
#usage:- ports- Enter the port number you want to scan separated by a comma for example:- -p 20,21,22 (scans port 20,21,22 for the above ip addresses)
#usage:- 'python portscanner_ir.py -h 172.29.43.* -p 20,21,23'
#Run in a linux or ubuntu terminal
import optparse
import socket
def connect(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s=socket.socket()	
		s.connect((ip,port))	
		banner=s.recv(1024)
		print "[+] Success"
		return banner
	except Exception,e :
		print "[-] Error "+str(e)
		return 


def main():
	parser=optparse.OptionParser('usage%prog '+' -H <ip address range e.g. 192.168.65.*> -p <target ports separated by comma> ')
	parser.add_option('-H', dest="t1host" , type="string" , help="specify target host range")
	parser.add_option('-p' , dest="t1port" , type="string" , help="specify target port separated by ',' ")
	(options,args)=parser.parse_args()
	t1host=options.t1host
	t1port=options.t1port
	tports = str(options.t1port)
	tports=tports.split(',')
	ip1=str(t1host).strip('*')
	if (t1host == None) | (t1port == None):
		print parser.usage
		exit(0)
	for x in range(1,255):
		ip= ip1+str(x)
		for port in tports:
			print "[+] Scanning ip:- "+str(ip)+" port:- "+str(port)
			banner=connect(ip,int(port));
			if banner:
				iplog.append(ip)
				portlog.append(port)
				print "[+] "+ip+" : "+banner
	

if __name__ == "__main__":
	main()

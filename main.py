import argparse
import socket
import sys

parser = argparse.ArgumentParser(description="My simple IRC logger")
parser.add_argument("-s","--network",help="Enter the name of the IRC network to join",metavar='')
parser.add_argument("-p","--port",type=int,help="Enter the port to connect",metavar='')
parser.add_argument("-c","--channel",help="Enter the IRC channel to join on the server",metavar='')
parser.add_argument("-n","--nick",help="Enter the nick to use",metavar='')
parser.add_argument("-o","--output",help="Enter the filename to write the chat log", metavar='')
args = parser.parse_args()

if args.network:
	network = args.network
else:
	network = raw_input("Enter the IRC network to join: ")
if args.port:
	port = args.port
else:
	port = int(raw_input("Enter the port to connect with: "))
if args.channel:
	channel = args.channel
else:
	channel = raw_input("Enter the channel to connect with: ")
if args.nick:
	nick = args.nick
else:
	nick = raw_input("Enter the nick to use: ")

try:
	irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
	print 'Failed to create socket. Error code: ' + str(msg[0]) + ', Error message: ' + msg[1]
	sys.exit();

try:
	irc.connect((network,port))
	print "Successful connection to network"
except socket.error, msg:
	print 'Failed to connect to the network. Error code: ' + str(msg[0]) + ', Error message: ' + msg[1]

print irc.recv(4096)
irc.send('NICK '+nick+'\r\n')
irc.send('USER hello hello hello : GOD IRC\r\n')
irc.send('JOIN ' + channel + '\r\n')

while True:
	data = irc.recv(4096)
	print "<" + data.split(':')[1].split('!')[0] + "> " + ":".join((data.split(':'))[2:]),
	if data.find('PING') != -1:
		irc.send('PONG ' + data.split()[1] + '\r\n')
import argparse

parser = argparse.ArgumentParser(description="My simple IRC logger")
parser.add_argument("-s","--server",help="Enter the name of the IRC server to join")
parser.add_argument("-p","--port",help="Enter the port to connect")
parser.add_argument("-c","--channel",help="Enter the IRC channel to join on the server")
parser.add_argument("-n","--nick",help="Enter the nick to use")
args = parser.parse_args()

if args.server:
	server = args.server
else:
	server = raw_input("Enter the IRC server to join: ")
if args.port:
	port = args.port
else:
	port = raw_input("Enter the port to connect with: ")
if args.channel:
	channel = args.channel
else:
	channel = raw_input("Enter the channel to connect with: ")
if args.nick:
	nick = args.nick
else:
	nick = raw_input("Enter the nick to use: ")

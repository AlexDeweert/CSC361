from socket import *
import time

# msg = "\r\n I love computer networks!"
# endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ('smtp.uvic.ca',25)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(5)

try:
	clientSocket.connect(mailserver)
	recv = clientSocket.recv(1024).decode()
	print(recv)
	if recv[:3] != '220':
		print('220 reply not received from server.')
except timeout:
	print ('Timeout trying to connect to to mailserver')

try:
	# Send HELO command and print server response.
	heloCommand = 'HELO alexand\r\n'
	clientSocket.send(heloCommand.encode())
	recv1 = clientSocket.recv(1024).decode()
	print(recv1)
	if recv1[:3] != '250':
		print('250 reply not received from server (HELO alexand).')
	#time.sleep(2)
except timeout:
	print ('Timeout trying to send HELO command')

try:
	# Send MAIL FROM command and print server response.
	mailFromCommand = 'mail from: alexand@uvic.ca\r\n'
	clientSocket.send(mailFromCommand.encode())
	recv2 = clientSocket.recv(1024).decode()
	if recv2[:3] != '250':
		print('250 reply not received from server (mail from alexand@uvic.ca)')
	#time.sleep(2)
except timeout:
	print ('Timeout trying to send mail from command')

try:
	# Send RCPT TO command and print server response.
	rcptToCommand = 'rcpt to: <alexander.deweert@gmail.com>\r\n'
	clientSocket.send(rcptToCommand.encode())
	recv3 = clientSocket.recv(1024).decode()
	print(recv3)
	if recv3[:3] != '250':
		print ('250 reply not received from server (rcpt to: <alexaner.deweertd@gmail.com)')
	#time.sleep(2)
except timeout:
	print ('Timeout trying to rctp to command')

try:
	# Send DATA command and print server response.
	dataCommand = 'data\r\n'
	clientSocket.send(dataCommand.encode())
	recv4 = clientSocket.recv(1024).decode()
	print(recv4)
	#if recv4[:3] != '354':
	#	print ('354 reply not received from server (data)')
	#time.sleep(2)
except timeout:
	print ('Timeout exception trying to send data command')

try:
	# Send message data.
	messageCommand = 'Subject: '
	messageCommand = messageCommand + raw_input('Enter subject: ')
	messageCommand.replace('\n','').replace('\r','')
	messageCommand = messageCommand + '\r\n' + raw_input('Type email message: ')
	#messageCommand.replace('\n','').replace('\r','')
	messageCommand = messageCommand + '\r\n'
	clientSocket.send(messageCommand.encode())
	#recv5 = clientSocket.recv(1024).decode()
	#print(recv5)
	#if recv4[:3] != '354':
	#	print ('354 reply not received from server (data)')
	#time.sleep(2)
except timeout:
	print ('Timeout exception trying to send e-mail message')

try:
	# Message ends with a single period.
	periodCommand = '.\r\n'
	clientSocket.send(periodCommand.encode())
	recv6 = clientSocket.recv(1024).decode()
	print(recv6)
	#if recv6[:3] != '354':
	#	print ('250 reply not received from server (single period)')
	#time.sleep(2)
except timeout:
	print ('Timeout exception trying to send period')

	# Send QUIT command and get server response.
	quitCommand = 'quit\r\n'
	clientSocket.send(quitCommand.encode())
	recv7 = clientSocket.recv(1024).decode()
	print(recv7)

	clientSocket.close()
	#if recv7[:3] != '221':
	#	print ('221 reply not received from server (quit)')

from socket import *

# msg = "\r\n I love computer networks!"
# endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = smtp-relay.gmail.com

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':t
	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO alexand\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server (HELO alexand).')

# Send MAIL FROM command and print server response.
mailFromCommand = 'mail from: alexand@uvic.ca\r\n'
clientSocket.send(heloCommand.encode())
recv2 = clientSocket.recv(1024).decode()
if recv2[:3] != '250':
	print('250 reply not received from server (mail from alexand@uvic.ca)')

# Send RCPT TO command and print server response.
rcptToCommand = 'rcpt to: <alexander.deweert@gmail.com>\r\n'
clientSocket.send(rcptToCommand.encode())
recv3 = clientSocket.recv(1024).decode()
if recv3[:3] != '250':
	print ('250 reply not received from server (rcpt to: <alexand@uvic.ca)')


# Send DATA command and print server response.
dataCommand = 'data\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
if recv4[:3] != '354':
	print ('354 reply not received from server (data)')

# Send message data.
messageCommand = 'Replace this text with a command line email message\r\n'
clientSocket.send(messageCommand.encode())
#recv5 = clientSocket.recv(1024).decode()
#if recv4[:3] != '354':
#	print ('354 reply not received from server (data)')

# Message ends with a single period.
periodCommand = '.\r\n'
clientSocket.send(periodCommand.encode())
recv6 = clientSocket.recv(1024).decode()
if recv6[:3] != '354':
	print ('250 reply not received from server (single period)')

# Send QUIT command and get server response.
quitCommand = 'quit\r\n'
clientSocket.send(quitCommand.encode())
recv7 = clientSocket.recv(1024).decode()
if recv7[:3] != '221':
	print ('221 reply not received from server (quit)')

import socket   #for sockets
import sys  #for exit
import time
import datetime

# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.settimeout(1.0)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

host = '10.0.0.1';
port = 12000;

#Need to send "ping sequence_number time" packets to server
#Send ping if:
#-sequence number is 0
#-or we get a response (acknowlegement) from server
#-or we don't get a reponse and we timeout (after 1 second)
i = 0
printfirst = 1
sendtime = 0
endtime = 0
deltatime = 0

while( i <= 10 ) :
    #print ' i : ' + str(i)
    msg = "ping " + str(i) + ' ' +  datetime.datetime.now().strftime("%X")
    
    if printfirst == 1:
        print 'Ping ' + host + ': ' + str(port)
        printfirst = 0

    try :
        #Set the whole string
        sendtime = datetime.datetime.now()
	#start time
	sendtime = int(round(time.time()*1000))
        s.sendto(msg, (host, port))
        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        #receivetime
        endtime = int(round(time.time()*1000))
	deltatime = endtime - sendtime
	reply = d[0]
        #addr = d[1]

        print  reply + ' time: ' + str(deltatime) + ' ms'

        i = i + 1
        time.sleep(1)

    except socket.timeout, msg:
        print 'Request timed out'
        i = i + 1

    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

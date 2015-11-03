import serial
import time

port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=3.0)

send = "nope"
out = ""


preamble = "@253" #attention + address
command = ""
terminator = ";FF"

print "hello mks program"

while not "quit" in send:



	send = raw_input("send: ")
	port.write(send)
 	#recieve = port.read(10)
	#print "recieved: " + recieve

	

	time.sleep(1)
	
	while port.inWaiting() > 0:
		out += port.read(1)
			
	print "rcvd: " + out
	
	out = ""


port.close()

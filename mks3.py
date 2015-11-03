import serial
import time

port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=3.0)



out = ""

preamble = "@253" #attention character + address
command = ""
terminator = ";FF"


outputfile = open("mksdata.txt", "a")

print "hello mks program"
outputfile.write("\nstart\n")


delay = 1
stop = time.time()+delay

#for i in range(0, 100):
while time.time() < stop:



	command = "PR1?"

	assemble = preamble + command + terminator	
	port.write(assemble)

	print "sent: " + assemble

	time.sleep(.1)
	
	while port.inWaiting() > 0:
		out += port.read(1)
		
	out = out.replace("@253ACK","")
	out = out.replace(";FF","")
	

	print "rcvd: " + out
	outputfile.write(out + "\n")
	
	out = ""


port.close()
outputfile.close()

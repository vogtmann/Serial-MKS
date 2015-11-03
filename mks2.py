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

	#if "" in send:
	#	command = ""

	if "baud" in send:
		command = "BR?"


	if "address" in send:
		command = "AD?"
	
	if "unit" in send:
		command = "U?"

	if "tag" in send:
		command = "UT?"

	if "version" in send:
		command = "FV?"

	if "pressure" in send:
		command = "PR1?"

	if "temp" in send:
		command = "TEM?"

	if "setpoint" in send:
		command = "EN1?"

	if "gas" in send:
		command = "GT?"
	
	if "quit" in send:
		command = "PR1?"

	assemble = preamble + command + terminator	
	port.write(assemble)
	print "sent: " + assemble

	time.sleep(1)
	
	while port.inWaiting() > 0:
		out += port.read(1)
			
	print "rcvd: " + out
	
	out = ""


port.close()

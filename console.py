#without serial commands

#commands:
#r refresh
#a send arbitrary command
#p poll pressure data
#s save pressure data
#q quit

#pgup/pgdn to scroll the pressure window

#import serial
import time
import curses
import threading

def update_pressure(data_logging_window):
	data_logging_window.clear()
	for x in range(0,10):
		
		time.sleep(1)	
		data_logging_window.addstr(get_pressure_data())
		data_logging_window.refresh()
		

	

def get_MKS_data():
	return_data = ""
	return_data += "address: \n"		#AD?
	return_data += "baud: \n"		#BR?
	return_data += "units: \n"		#U?	
	return_data += "tag: \n"		#UT?
	return_data += "Firmware Version: \n"	#FV?
	return_data += "Gas Type: \n"		#GT?
	return_data += "Setpoint: \n"		#EN1?
	return_data += "Temperature: \n"	#TEM?
	return_data += "Pressure: \n"		#PR1
	
	return return_data

def get_pressure_data():
	return_data = ""
	return_data += "Pressure:\t9.00E2\n"
	return return_data

def loop(data_window, data_text_window, data_logging_window, stdscr):

	continuing = 1

	c = data_window.getch()


	if c == ord('r') or c == ord('R'):
		data_text_window.clear()
		data_text_window.addstr("Getting MKS data...", curses.color_pair(3))
		data_text_window.refresh()
		
		data_text_window.clear()
		data_text_window.addstr(get_MKS_data())

	elif c == ord('p') or c == ord('P'):
		data_logging_window.clear()
		data_logging_window.addstr("Starting log...")
		data_logging_window.refresh()		

		pressure = threading.Thread(target=update_pressure, args=(data_logging_window,))
		pressure.daemon = True
		pressure.start()



	elif c == ord('q') or c == ord('Q'):
		continuing = 0

	
	#refresh windows
	stdscr.noutrefresh()
	data_window.noutrefresh()
	data_text_window.noutrefresh()

		

	curses.doupdate()

	return continuing


def main(stdscr):
	curses.curs_set(0)
	

	#some color choices
	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)

	#header
	stdscr.addstr("MKS INTERFACE", curses.A_REVERSE)
	stdscr.chgat(-1, curses.A_REVERSE)

	stdscr.addstr(curses.LINES-1, 0, "'r' to refresh, 'p' to poll, 'q' to quit")


	# green r, blue p, red q
	stdscr.chgat(curses.LINES-1, 1, 1, curses.A_BOLD | curses.color_pair(2))
	stdscr.chgat(curses.LINES-1, 17, 1, curses.A_BOLD | curses.color_pair(3))
	stdscr.chgat(curses.LINES-1, 30, 1, curses.A_BOLD | curses.color_pair(1))
	

	#window to display gauge setup
	data_window = curses.newwin(curses.LINES-2, curses.COLS, 1, 0)

	#border windows
	data_text_border_window = data_window.subwin(curses.LINES-6, (curses.COLS-4)/2, 3, 2)
	data_logging_border_window = data_window.subwin(curses.LINES-6, (curses.COLS-4)/2, 3, (curses.COLS-4)/2 + 2)

	
	#creating subwindow to cleanly display text without touching window's borders
	data_text_window = data_text_border_window.subwin(curses.LINES-8, (curses.COLS-6)/2-1, 4, 3)


	#subwindow for showing pressure log
	data_logging_window = data_logging_border_window.subwin(curses.LINES-8, (curses.COLS-6)/2-1, 4, (curses.COLS-4)/2 + 3)

	#draw a box around main window
	data_window.box()

	data_text_border_window.box()
	data_logging_border_window.box()

	data_text_window.addstr("Press 'r' to load data")
	data_logging_window.addstr("Press 'p' to log pressure data here")

	#update internal curses structures
	stdscr.noutrefresh()
	data_window.noutrefresh()

	#redraw screen
	curses.doupdate()

	while True:
		if not loop(data_window, data_text_window, data_logging_window, stdscr):
			break



send = ""
out = ""


preamble = "@253" #attention + default address, needed even with RS232
command = ""
terminator = ";FF"

curses.wrapper(main)


#Serial port communication
#	port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=3.0)
#	assemble = preamble + command + terminator	
#	port.write(assemble)
#	time.sleep(1)
#	while port.inWaiting() > 0:
#		out += port.read(1)
#	port.close()



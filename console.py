#without serial commands

#commands:
#r refresh
#a send arbitrary command
#p poll pressure data
#s save pressure data
#q quit

#import serial
#import time
import curses


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



send = ""
out = ""


preamble = "@253" #attention + default address, needed even with RS232
command = ""
terminator = ";FF"


#Serial port communication
#	port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=3.0)
#	assemble = preamble + command + terminator	
#	port.write(assemble)
#	time.sleep(1)
#	while port.inWaiting() > 0:
#		out += port.read(1)
#	port.close()


stdscr = curses.initscr()

#initialize screen
curses.noecho()
curses.cbreak()
curses.curs_set(0)

if curses.has_colors():
	curses.start_color()

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
data_logging_border_window = data_window.subwin(curses.LINES-6, (curses.COLS-4)/2, 3, 

(curses.COLS-4)/2 + 2)



#creating subwindow to cleanly display text without touching window's borders
data_text_window = data_text_border_window.subwin(curses.LINES-8, (curses.COLS-6)/2-1, 4, 

3)


#subwindow for showing pressure log
data_logging_window = data_logging_border_window.subwin(curses.LINES-8, (curses.COLS-6)/2-

1, 4, (curses.COLS-4)/2 + 3)




#data_text_window.addstr("Press 'R' to load data")
#data_logging_window.addstr("Press 'P' to log here")


#draw a box around main window
data_window.box()

data_text_border_window.box()
data_logging_border_window.box()

#data_logging_window.box()
#data_text_window.box()


data_text_window.addstr("Press 'r' to load data")
data_logging_window.addstr("Press 'p' to log here")


#update internal curses structures
stdscr.noutrefresh()
data_window.noutrefresh()

#redraw screen
curses.doupdate()

while True:
	c = data_window.getch()

	if c == ord('r') or c == ord('R'):
		data_text_window.clear()
		data_text_window.addstr("Getting MKS data...", curses.color_pair(3))

		data_text_window.refresh()
		data_text_window.clear()
		data_text_window.addstr(get_MKS_data())

	elif c == ord('q') or c == ord('Q'):
		break

	
	#refresh windows
	stdscr.noutrefresh()
	data_window.noutrefresh()
	data_text_window.noutrefresh()
	curses.doupdate()


#restore terminal settings
curses.nocbreak()
curses.echo()
curses.curs_set(1)

curses.endwin()

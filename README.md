# Serial-MKS

This project is to connect with the MKS 925c using its serial interface. It probably works with the regular 925 as well, but it's only tested on the 925c. It's also designed around the RS-232 varient.

The MKS 925C is a full range vacuum sensor. In one gauge it measures from atmospheric down to 1x10-5 torr. In addition to the serial interface, it also has an analog voltage out, and a relay activated by a setpoint.

###Files
- mks.py - sends arbitary commands to a specified address.
- mks2.py - a friendlier interface for sending some predefined commands.
- mks3.py - very simple pressure data logging.
- console.py - console application to monitor a vacuum gauge.

###Future goals
- a TUI to place all the information at once.
- better datalogging capabilities.

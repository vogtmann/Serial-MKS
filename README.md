# Serial-MKS

This project is to interface with the MKS 925c. It probably works with the regular 925 as well, but it's only tested on the 925c. It's also designed around the RS-232 varient.

The MKS 925C is a full range vacuum sensor. In one gauge it measures from atmospheric down to 1x10-5 torr.

It has a RS-232 serial interfaces, as well as a analog voltage out.

mks.py - sends arbitary commands to a specified address.
mks2.py - a friendlier interface for sending some predefined commands.
mks3.py - very simple pressure data logging

Future goals include a TUI to place all the information at once, as well as better datalogging capabilities.

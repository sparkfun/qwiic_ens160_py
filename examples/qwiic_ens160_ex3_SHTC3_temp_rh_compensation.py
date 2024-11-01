#!/usr/bin/env python
#-------------------------------------------------------------------------------
# qwiic_template_ex3_temp_rh_compensation.py
# 
# TODO: NOTE: THIS IS A PLACEHOLDER UNTIL THE LIBRARY HERE IS IMPLEMENTED: https://github.com/sparkfun/Qwiic_SHTC3_Py
#
#  This example shows how to give the ENS160 Temperature and Relative Humidity
# Data for compensation. Note that the values that are given for compensation are not
# populated in their registers until the Air Quality Sensor is set to "Standard" operation
# and when data is ready i.e. the data ready bit is set. Also note that there will be some 
# rounding of the temperature and relative humidity values when they're given to the sensor
# and again when they're read back. 
#
#-------------------------------------------------------------------------------
# Written by SparkFun Electronics, October 2024
#
# This python library supports the SparkFun Electroncis Qwiic ecosystem
#
# More information on Qwiic is at https://www.sparkfun.com/qwiic
#
# Do you like this library? Help support SparkFun. Buy a board!
#===============================================================================
# Copyright (c) 2024 SparkFun Electronics
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.
#===============================================================================

import qwiic_ens160
import sys

def runExample():
	# TODO Replace template and title
	print("\nQwiic ENS160 Example 3 - Humidity and Temperature Sensor Compensation - SHTC3\n")

	# Create instance of device
	myEns = qwiic_ens160.QwiicENS160()

	# Check if it's connected
	if myEns.is_connected() == False:
		print("The device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	# Initialize the device
	myEns.begin()

	# NOTE: 

	

if __name__ == '__main__':
	try:
		runExample()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Example")
		sys.exit(0)
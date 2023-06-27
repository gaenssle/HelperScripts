#!/usr/bin/python
# Written in Python 3.7 in 2023 by A.L.O. Gaenssle
# CONVERTER for tables
# -> changes column speparator from , to tabs

import sys


try:
	with open(sys.argv[1], 'r') as file:
		output_name = sys.argv[1].split(".")[0] + "_tabs.txt"
		output_file = open(output_name, "w")
		for line in file:
			line = line.replace(",", "\t")
			output_file.write(line)
except IndexError:
	print("Please provide a files as argument\n(e.g. python3 Commas_to_Tabs.py Test.txt)")
except FileNotFoundError:
	print("This file does not exist.\nPlease provide an existing file as argument")

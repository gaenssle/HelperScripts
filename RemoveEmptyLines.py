#!/usr/bin/python
# Written in Python 3.7 in 2023 by A.L.O. Gaenssle
# REMOVER of empty lines in a file

import sys

try:
	with open(sys.argv[1], 'r') as file:
		OutputName = sys.argv[1].split(".")[0] + "_condensed.txt"
		OutputFile = open(OutputName, "w")
		for line in file:
			if len(line) > 1:
				OutputFile.write(line)
except IndexError:
	print("Please provide a files as argument\n(e.g. python3 Remove_EmptyLines.py Test.txt)")
except FileNotFoundError:
	print("This file does not exist.\nPlease provide an existing file as argument")

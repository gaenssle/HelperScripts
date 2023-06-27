#!/usr/bin/python
# Written in Python 3.7 in 2023 by A.L.O. Gaenssle
# CONVERTER FOR DECIMAL & THOUSAND SEPARATORS

import sys
import re


# Check for numbers containing digits, and ".", "," or " " as separators
# Include numbers with leading +/-
is_number = re.compile("[\d., +-]+")


# Detect type of thousand and decimal separator and remove anything expect a dot for decimal separator
def DetectType(number):
	dot_comma = re.compile('[+-]?\d+(\.\d\d\d)*,\d+')
	comma_dot = re.compile('[+-]?\d+(,\d\d\d)*\.\d+')
	number = number.replace(" ", "")
	if dot_comma.fullmatch(number):
		return(number.replace(".","").replace(",", "."))
	elif comma_dot.fullmatch(number):
		return(number.replace(",",""))
	else:
		return(number)


# Check each line for numbers and convert them to the international format
def Convert(line):
	list_converted = []
	line_list = line.split("\t")
	for item in line_list:
		if is_number.fullmatch(item):
			item = DetectType(item)
		# item = decmark_reg.sub('.',item)
		list_converted.append(item)
	line_converted = "\t".join(list_converted)
	return(line_converted)


# Import, read and export the file
try:
	with open(sys.argv[1], 'r') as input_file:
		output_name = sys.argv[1].rsplit(".",1)[0] + "_internationalDecimals.txt"
		output_file = open(output_name, "w")
		for line in input_file:
			line = line.rstrip()
			if len(line) > 1:
				line_converted = Convert(line)
				output_file.write(line_converted)
				output_file.write("\n")
		print("Converted", sys.argv[1], "to international numbering\nSaved as:", output_name)
except IndexError:
	print("Please provide a file as argument\n(e.g. python3 Convert_Decimal_Separator.py Test.txt)")
except FileNotFoundError:
	print("This file does not exist.\nPlease provide an existing file as argument")

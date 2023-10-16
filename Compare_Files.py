#!/usr/bin/python
# Written in Python 3.7 in 2023 by A.L.O. Gaenssle
# COMPARES TWO LISTS
# -> Checks if each lines exists in the other file as well
# -> If not, it prints the line

import sys

def import_file(file):
	with open(file, 'r') as file:
		data = file.read().splitlines()
	return(data)

def get_missing(data1, data2):
    list = []
    count = 0
    for line in data2:
        if line not in data1:
            list.append(line)
            count += 1
    return(list)


try:
	data1 = import_file(sys.argv[1])
	data2 = import_file(sys.argv[2])
except IndexError:
	print("Please provide two files as argument\n(e.g. python3 Compare_Files.py Test.txt)")
	quit()
except FileNotFoundError:
	print("This file does not exist.\nPlease provide an existing file as argument")
	quit()


print(len(data1), len(data2))

list = get_missing(data1, data2)
print("\nMissing in File1:\t",len(list), "\n","\n".join(list))
list = get_missing(data2, data1)
print("\nMissing in File2:\t",len(list), "\n","\n".join(list))

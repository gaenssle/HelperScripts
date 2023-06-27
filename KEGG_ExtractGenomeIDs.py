#!/usr/bin/python
# Written in Python 3.7 in 2023 by A.L.O. Gaenssle
# EXTRACTER of KEGG Genome IDs from KEGG gene IDs
# -> Takes a list of KEGG gene IDs as input

import sys

def get_genomeIDs(data):
	list = []
	for item in data:
		ID = item.split(":",1)[0]
		if ID not in list:
			list.append(ID)
	return(list)


try:
	with open(sys.argv[1], 'r') as file:
		data = file.read().splitlines()
	list = get_genomeIDs(data)
	output_name = sys.argv[1].split(".")[0] + "_genomeIDs.txt"
	with open(output_name, "w") as output_file:
		output_file.writelines(line + '\n' for line in list)
except IndexError:
	print("Please provide a files as argument\n(e.g. python3 Commas_to_Tabs.py Test.txt)")
except FileNotFoundError:
	print("This file does not exist.\nPlease provide an existing file as argument")

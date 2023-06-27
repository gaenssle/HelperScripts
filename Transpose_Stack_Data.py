#!/usr/bin/python
# Written in Python 3.7 in 2023 by A.L.O. Gaenssle
# TRANSPOSER -> TABLE TO COLUMN PAIR

import sys
import pandas as pd


try:
	data = pd.read_csv(sys.argv[1], sep="\t")
	stacked = pd.melt(data, id_vars=data.columns[0], value_vars=data.columns[1:])

	# move sample column to front
	samples = stacked.pop(stacked.columns[1])
	stacked.insert(0,'Sample', samples)

	output_name = sys.argv[1].rsplit(".",1)[0] + "_stacked.txt"
	stacked.to_csv(output_name, sep="\t", index=False)
	print("Data was stacked to 3 columns", sys.argv[1], "\nSaved as:", output_name)
except IndexError:
	print("Please provide a file as argument\n(e.g. python3 Transpose_Stack_Data.py Test.txt)")
except FileNotFoundError:
	print("This file does not exist.\nPlease provide an existing file as argument")
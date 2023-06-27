#!/usr/bin/python
# Written in Python 3.7 in 2023 by A.L.O. Gaenssle
# TRANSPOSER -> COLUMN PAIR TO TABLE

import sys
import pandas as pd


try:
	data = pd.read_csv(sys.argv[1], sep="\t")
	unstacked = data.pivot(index=data.columns[1], columns=data.columns[0])[data.columns[-1]]
	output_name = sys.argv[1].rsplit(".",1)[0] + "_stacked.txt"
	unstacked.to_csv(output_name, sep="\t")
	print("Data from:", sys.argv[1], "was unstacked to", len(data.columns), "columns\nSaved as:", output_name)
except IndexError:
	print("Please provide a file as argument\n(e.g. python3 Transpose_Unstack_Data.py Test.txt)")
except FileNotFoundError:
	print("This file does not exist.\nPlease provide an existing file as argument")
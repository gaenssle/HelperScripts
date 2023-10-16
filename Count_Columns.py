#!/usr/bin/python
# Written in Python 3.7 in 2023 by A.L.O. Gaenssle
# COLUMN COUNTER

import sys
import pandas as pd
import argparse

## ------------------------------------------------------------------------------------------------
## INPUT ARGUMENTS --------------------------------------------------------------------------------
## ------------------------------------------------------------------------------------------------

parser = argparse.ArgumentParser(description="COLUMN COUNTER"
	"\nThis program reads in a provided file (.csv or .txt)"
	"\nCounts all columns given as argument")
parser.add_argument("file", 
	help="name of the file")
parser.add_argument("-ask", "--askoverwrite", 
	help="ask before overwriting files",
	action="store_true")
parser.add_argument("-c", "--columns", 
	help="enter column names to be counted, separated by ';' (e.g.Kingdom,Domain,Phylum) (default: %(default)s)", 
	default="-1")
parser.add_argument("-ft", "--filetype", 
	help="type of the generated files (default: %(default)s)", 
	default=".csv")
parser.add_argument("-sep", "--separator", 
	help="separator between columns in the output files (default: %(default)s)", 
	default=";")

args = parser.parse_args()

# Check if given list of column names is valid
while True:
	try:
		args.columns = args.columns.split(";")
		for cname in args.columns:
			try:
				canme = int(cname)
			except ValueError:
				pass
		break
	except IndexError:
		args.columns = input("\nCannot read given list of databases"
			"\nPlease enter the names of the databases separated by ';'"
			"\nWithout spaces but can be in lower case or caps\n")

# Check for tab separator
if args.separator in ["\\t", "tab", "'\\t'", "{tab}"]:
	args.separator = "\t"


## ------------------------------------------------------------------------------------------------
## FUNCTIONS --------------------------------------------------------------------------------------
## ------------------------------------------------------------------------------------------------
## ================================================================================================
## ================================================================================================
## Check if the file already exists and if it should be replaced
def CheckFileExists(FileName, Ask):
	if Ask:
		Replace = "n"
	else:
		Replace = "y"
	while Replace == "n":
		if not os.path.exists(FileName):
			break
		else:
			Replace = input("\nFile " + FileName + " already exits -> should it be replaced?"
				"\n(y=yes, n=no)\n")
			while Replace not in ("y", "n"):
				Replace = input("\nPlease enter 'y' or 'n'!\n")
		if Replace == "n":
			FileName = input("\nEnter a new filename\n")
	return(FileName)

## Export pandas dataframe
def ExportDataFrame(DataFrame, FileName, Add="", Columns="", 
	FileType=".csv", Sep=";", Ask=True, Header=True):
	FileName = FileName + Add + FileType
	FileName = CheckFileExists(FileName, Ask)
	if Columns == "":
		Columns = list(DataFrame)
	DataFrame.to_csv(FileName, sep=Sep, columns = Columns, index=False, header=Header)
	print("File saved as:", FileName, "\n")



## ------------------------------------------------------------------------------------------------
## SCRIPT -----------------------------------------------------------------------------------------
## ------------------------------------------------------------------------------------------------
TargetColumns = args.columns

try:
	data = pd.read_csv(args.file, sep=args.separator)
	colIndex = list(data.columns.get_indexer(args.columns))
	ReferenceColumns = list(data.columns[0:min(colIndex)])
	data = data.groupby(ReferenceColumns, as_index=False)[TargetColumns].count()
	print(data[:10])
	ExportDataFrame(data, args.file, Add="_count", 
		FileType=args.filetype, Sep=args.separator, Ask=args.askoverwrite)
except IndexError:
	print("Please provide a file as argument\n(e.g. python3 Transpose_Stack_Data.py Test.txt)")
except FileNotFoundError:
	print("This file does not exist.\nPlease provide an existing file as argument")

			
#!/bin/python3
from os import listdir
import sys
import pandas as pd
import numpy as np

# FUNCITON TO EXTRACT CSV FILES
def find_csv_filenames(path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ "data/"+filename for filename in filenames if filename.endswith( suffix ) ]

files = find_csv_filenames("data/")

# Adding the DataFrames to an list
dfs = [pd.read_csv(x) for x in files]

# Empty List for names
fname = []
mname = []
lname = []

# Data Cleaning and preprocessing
tdf = pd.DataFrame()
for df in dfs:
    m = df['student_name'].str.replace('   ',' ').str.replace('  ', ' ').str.split(' ', expand=True)
    tdf = pd.concat([tdf, m], axis=0)

# tdf.to_csv('tmp.csv', index=False)

tdf = tdf.fillna('').values

# Condition for extracting First, Middle and Last names
for x in tdf:
    x = list(x)
    x = list(filter(None, x))
    print(x)
    
    if len(x) == 1:
        fname.append(x[0].strip().lower())

    elif len(x) == 2:
        fname.append(x[0].strip().lower())
        lname.append(x[1].strip().lower())

    elif len(x) == 3:
        fname.append(x[0].strip().lower())
        mname.append(x[1].strip().lower())
        lname.append(x[2].strip().lower())

    elif len(x) == 4:
        fname.append(x[0].strip().lower())
        mname.append(x[1].strip().lower())
        mname.append(x[2].strip().lower())
        lname.append(x[3].strip().lower())

    elif len(x) == 5:
        fname.append(x[0].strip().lower())
        mname.append(x[1].strip().lower())
        mname.append(x[2].strip().lower())
        mname.append(x[3].strip().lower())
        lname.append(x[4].strip().lower())

    
# Removing Duplicates by converting to SET
fname = set(fname)
mname = set(mname)
lname = set(lname)

# Saving output files
with open('result/1_first_name.txt', 'w') as f:
    for line in fname:
        f.write("%s\n" % line)

with open('result/2_middle_name.txt', 'w') as f:
    for line in mname:
        f.write("%s\n" % line)

with open('result/3_last_name.txt', 'w') as f:
    for line in lname:
        f.write("%s\n" % line)


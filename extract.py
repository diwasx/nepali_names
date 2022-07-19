#!/bin/python3
from os import listdir
import pandas as pd

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

# Looping Through DataFrames
for df in dfs:
    for i in df['student_name'].str.split(' ', expand=True)[0]:
        fname.append(i.strip().lower())

    for i in df['student_name'].str.split(' ', expand=True)[1]:
        mname.append(i.strip().lower())

    for i in df['student_name'].str.split(' ', expand=True)[2]:
        try:
            lname.append(i.strip().lower())
        except:
            lname.append(i)

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


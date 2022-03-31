import sys
import csv
import os

first_file = True

for i in range(1, len(sys.argv)):
    cur_path = sys.argv[i]
    cur_file = open(cur_path)
    cur_csvreader = csv.reader(cur_file)
    header = str(next(cur_csvreader)).strip(
        "[]").replace("'", "") + ", filename"
    # if this is our first file, then we need to write the header to our output csv file
    if first_file:
        print(header)
        first_file = False
    for i in cur_csvreader:
        print(str(i).strip("[]").replace(
            "'", "") + ", " + str(os.path.basename(cur_path)))
    cur_file.close()

import csv

# provide the filename 
file_name = "brown.csv"

# open file for reading
with open(file_name, newline='') as infile:
    # read csv into `reader` as a dictionary

    # open output file `brown.dict`
    with open('brown.dict', 'w') as outfile:
        # output file contains a list of dictionaries
        outfile.write(f"[\n")


        outfile.write(f"]\n")
import csv

# provide the file name and the fieldnames (keys) of dictionary
file_name = "brown-grades.dict"
field_names = 

# the dict we want to turn into a CSV
grades_dict = [
    {'date': '3/12', 'student': 'Cindy Who', 'class': 'English1', 'teacher': 'Brown', 'grade': 'A'},
    {'date': '3/12', 'student': 'Charlie Brown', 'class': 'English1', 'teacher': 'Brown', 'grade': 'A'},
    {'date': '3/12', 'student': 'Melvin Arnold', 'class': 'English', 'teacher': 'Brown', 'grade': 'B'},
    {'date': '3/12', 'student': 'Jennifer Buckle', 'class': 'English1', 'teacher': 'Brown', 'grade': 'B'},
    {'date': '3/12', 'student': 'Peppermint Patty', 'class': 'English1', 'teacher': 'Brown', 'grade': 'A'},
]

# open the file for writing
with open('brown-grades.csv', 'w') as csvfile:

    # insert csv header


     # write the csv rows
import csv

def csv2dict(filename):

    # open file and create DictReader object
    with open(filename, newline="") as infile:
        pass

        # object to hold results
        data_dict = []
        # append rows from read_csv to data_dict
        pass

        # return data_dict

def dict2csv(filename, fieldnames, data):

    with open(filename, "w", newline="") as outfile:
        pass

def main():

    # test csv to dict conversion
    student_data_file = "student_data.csv"
    data_dict = csv2dict(student_data_file)
    print(data_dict)

    # test result
    expected_dict = [{'date': '3/12', 'student': 'Cindy Who', 'class': 'English1', 'teacher': 'Brown', 'grade': None}, {'date': '3/12', 'student': 'Charlie Brown', 'class': 'English1', 'teacher': 'Brown', 'grade': None}, {'date': '3/12', 'student': 'Melvin Arnold', 'class': 'English', 'teacher': 'Brown', 'grade': None}, {'date': '3/12', 'student': 'Jennifer Buckle', 'class': 'English1', 'teacher': 'Brown', 'grade': None}, {'date': '3/12', 'student': 'Peppermint Patty', 'class': 'English1', 'teacher': 'Brown', 'grade': None}]
    assert data_dict == expected_dict, "the returned data does not match the expected dict"

    # test dict to csv conversion
    filename = "student_grades.csv"
    fieldnames = ["date", "student", "class", "teacher", "grade"]

    # add grades to simulate grades added by teacher
    for item in data_dict:
        item["grade"] = "A"

    dict2csv(filename, fieldnames, data_dict)

    # test result
    with open("student_grades.csv", "r") as infile:
        check_data = infile.read()
        print(check_data)
    expected_data = """date,student,class,teacher,grade\n3/12,Cindy Who,English1,Brown,A\n3/12,Charlie Brown,English1,Brown,A\n3/12,Melvin Arnold,English,Brown,A\n3/12,Jennifer Buckle,English1,Brown,A\n3/12,Peppermint Patty,English1,Brown,A\n"""
    assert check_data == expected_data, "the written data does not match the expected data"

if __name__ == "__main__":
    main()


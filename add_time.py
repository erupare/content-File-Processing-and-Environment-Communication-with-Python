from datetime import datetime, timedelta

# due date data from db
title_due_dates = [
    ["Oh Python! My Python!", "2020-11-15"],
    ["Fun with Django", "2020-06-23"],
    ["When Bees Attack! The Horror!", "2020-12-10"],
    ["Martin Buber's Philosophies", "2020-07-12"],
    ["The Sun Also Orbits", "2020-10-31"]
]

# replace the string date with a date object for each title
# add the last minute of day to each due date
# add a timedelta representing the last minute of the day
pass # student code here


# replace the datetime object with a string representation
# remember SQLite stores dates as strings
pass # student code here

# test 
expected_list = [['Oh Python! My Python!', '2020-11-15 23:59:00'], ['Fun with Django', '2020-06-23 23:59:00'], ['When Bees Attack! The Horror!', '2020-12-10 23:59:00'], ["Martin Buber's Philosophies", '2020-07-12 23:59:00'], ['The Sun Also Orbits', '2020-10-31 23:59:00']]
assert title_due_dates == expected_list
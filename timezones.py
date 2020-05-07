import pytz
from datetime import datetime

# due date data from db
title_due_dates = [
    ['Oh Python! My Python!', '2020-11-15 23:59:59'], 
    ['Fun with Django', '2020-06-23 23:59:59'], 
    ['When Bees Attack! The Horror!', '2020-12-10 23:59:59'], 
    ["Martin Buber's Philosophies", '2020-07-12 23:59:59'], 
    ['The Sun Also Orbits', '2020-10-31 23:59:59']
]

# dictionary matching the timezone value to book title
title_time_zones = {
    'Oh Python! My Python!': 'US/Central', 
    'Fun with Django': 'US/Pacific', 
    'When Bees Attack! The Horror!': 'Europe/London', 
    "Martin Buber's Philosophies": 'Australia/Melbourne', 
    'The Sun Also Orbits': 'Europe/Paris'
}

# when the db due_date string is converted to a datetime object it is naive
# it does not contain timezone info
# make the due_date timezone aware with `<due_date>.replace(timezone)`
# make the timezone the same as indicated in `title_time_zones`
# this makes the book due just before midnight local time
pass # student code

# aware_title_due_dates has the due date in the author's timezone
# following good db practice we will store the dates as UTC and
# only convert when necessary to time zone needed
# update `title_due_dates` with the due_date in UTC time
pass # student code

# we can now use title_due_dates for updating the db
expected_results = [['Oh Python! My Python!', '2020-11-16 05:50:59 UTC+0000'], ['Fun with Django', '2020-06-24 07:52:59 UTC+0000'], ['When Bees Attack! The Horror!', '2020-12-11 00:00:59 UTC+0000'], ["Martin Buber's Philosophies", '2020-07-12 14:19:59 UTC+0000'], ['The Sun Also Orbits', '2020-10-31 23:50:59 UTC+0000']]
assert title_due_dates == expected_results, f"Expected: {expected_results}\nGot: {title_due_dates}"

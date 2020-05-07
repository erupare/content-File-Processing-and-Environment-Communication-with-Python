import configparser

# data to be used
data_list = [
    ["author", "title", "pages", "due_date", "genre", "isbn"],
    ["Thompson, Keith", "Oh Python! My Python!", 1200, "2020-11-15", "biography", "000-1-000000-00-1"],
    ["Fritts, Larry", "Fun with Django", 150, "2020-06-23", "satire", "00-2-000000-00-2"]
]

novel_text = "Numquam labore labore tempora. Dolore dolorem quisquam aliquam eius dolor non ipsum. Dolorem est velit tempora quaerat. Est magnam porro voluptatem dolore. Adipisci voluptatem consectetur dolore voluptatem voluptatem neque. Adipisci non modi quiquia etincidunt quisquam. Etincidunt consectetur dolore ut. Quaerat ut adipisci sit aliquam quisquam ut. Voluptatem labore porro porro.\n\nPorro modi numquam non sed dolor. Consectetur dolor adipisci quaerat aliquam adipisci. Etincidunt porro modi dolor neque numquam magnam neque. Ipsum consectetur ut eius ut. Dolor ut modi non est tempora labore sit.\n\nEtincidunt voluptatem quaerat consectetur sed est etincidunt ipsum. Ut adipisci numquam etincidunt porro porro. Dolore eius modi aliquam. Velit amet sed quaerat etincidunt est. Ut consectetur modi ipsum sed aliquam. Amet tempora quiquia eius voluptatem aliquam dolore ut. Etincidunt dolor non voluptatem eius sed non adipisci."

# use configparser to create the configuration file as described in the instructions
# write the file to printer_config.ini
pass # student code here


# test
try:
    with open("printer_config.ini", "r") as f:
        config_text = f.read()
except FileNotFoundError:
        config_text = ""

with open("test_printer_config.ini", "r") as f:
    expected_text = f.read()

assert config_text == expected_text
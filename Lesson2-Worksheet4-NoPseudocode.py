# Lesson 2 - Strings
# Worksheet 4
# Problem: Create a username validator
# Requirements:
#
# Between 5-15 characters
# Only letters and numbers
# Must start with a letter
username = input("please enter a username: ")

def username_check():
    username_pass = 0
    if username >= 5:
        username_pass = username_pass + 1
    elif username <= 15:
        username_pass += username_pass + 1

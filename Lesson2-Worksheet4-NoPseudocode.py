# Lesson 2 - Strings
# Worksheet 4
# Problem: Create a username validator
# Requirements:
#
# Between 5-15 characters
# Only letters and numbers
# Must start with a letter

def username_check(username):
    if not len(username) >= 5 or not len(username) <= 15:
        return "Username must be 5-15 characters"
    if not username[0].isalpha():
        return "Username must start with a letter"
    if not username.isalnum():
        return "Username can only contain letters and numbers"
    else:
        return "valid username"
    
username = input("please enter a username: ")
username_check(username)
print(username_check(username))

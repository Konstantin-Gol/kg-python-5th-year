#section 2.2
def password_check(): #makes a chunk of code for later use or reuse
    if len(password) < 8:#checks if text is less than eight
        print("Password is too short (must contain at least 8 characters)")#len() makes the length of the string into an interger
    else:
        print("Password length is valid")
    if password.isalnum() and password.isalpha(): #checks for both letters and numbers
        print("Password must contain at least one digit")
    else:
        print("password contains a digit")

password = input("Enter Password: ")
password_check()#always call
#section 2.1
text = input("please enter 2 words: ")
print("uppercase: ", text.upper())#forces text to be uppercase
print("lowercase: ", text.lower())#forces text to be lowercase
print("number of chars in string: ", len(text)) #counts all charecters including spaces
print("position of first space: ", text.find(" "))#finds the first space
print("is the sentance all lowercase: ", text.islower())#checks of the text is all lowercase
print("all spaces replaced with underscores: ", text.replace(" ", "_"))#replaces space with underscores
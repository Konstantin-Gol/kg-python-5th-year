# Date: Oct 25
# Author: Ms Hayes
# Purpose: Iteration with Strings - Teacher Example
# Connect to iteration and repetition keywords.
 
word = "Python"
 
# Iterate through each character
for letter in word:
    print(letter)
 
# Count vowels and consonants using iteration
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
count = 0
count2 = 0
for letter in word.lower():
    if letter in vowels:
        count += 1
    if letter in consonants:
        count2 += 1
        
print("Number of vowels: ", count)
print('Number of consonants', count2)
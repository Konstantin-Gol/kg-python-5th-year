# Lesson 2 - Strings
# Worksheet 3
# Tier 1: Complete tasks 1-2 - check answers
# Tier 2: Complete tasks 3-4 - check answers
# Tier 3: Complete tasks 5 - check answers

#
# Tier 1 - Complete Tasks 1-2
#

# Task 1: Count vowels in a word
text = "algorithm"
vowels = "aeiou"
vowel_count = 0

# Complete this code
for letter in text:
    if letter in vowels:
        vowel_count = vowel_count + 1  # Add 1 to the count
    
print("Vowels found:", vowel_count)

# Task 2: Now try with a different word:
text2 = "computer"
vowel_count2 = 0
# Write the complete code yourself:
for letter in text:
    if letter in vowels:
        vowel_count2 = vowel_count2 + 1
print("Vowels found:", vowel_count2)

#
# Tier 2 - Complete Tasks 3-4
#

# Task 3: Count consonants (letters that are NOT vowels)
text = "programming"
vowels = "aeiou"
consonant_count = 0

# Write your code here:
for letter in text:
    if letter not in vowels:
        consonant_count = consonant_count + 1
print("Consonants found:", consonant_count)

# Task 4: Count how many uppercase and lowercase letters separately
text2 = "LeavingCert"
uppercase_count = 0
lowercase_count = 0
uppercase = letter = text2.isupper()
lowercase = letter = text2.islower()
# Write your code here:
for letter in text2:
    if letter in uppercase:        
        uppercase_count += 1
    if letter in lowercase:
        lowercase_count += 1
print("Lowercase letters found:", uppercase_count)
print("Uppercase letters found:", lowercase_count)
#
# Tier 3 - Complete Tasks 5
#

# Task 5: Create a character frequency counter
text = "algorithm"

# Your output should look like this:
# a: 1
# l: 1
# g: 1
# o: 1
# r: 1
# i: 1
# t: 1
# h: 1
# m: 1

# Hint: You might want to use a dictionary or count each letter individually
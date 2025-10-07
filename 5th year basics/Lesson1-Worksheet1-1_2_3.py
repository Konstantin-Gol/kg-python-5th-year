# Lesson 1 - Strings
# Worksheet 1
# Tier 1: Complete tasks 1-5 - check answers
# Tier 2: Complete tasks 6-9 - check answers
# Tier 3: Complete tasks 10-11 - check answers

#
# Tier 1 - Complete Tasks 1-5
#

course = "LeavingCertComputerScience"

# Example completed for you:
example = course[0:7]  # "Leaving"

# 1. Extract "Cert" (starts at position 7, ends at 11)
answer1 = course[7:11]  # "Cert"

# 2. Extract "Computer" (starts at position 11, ends at 19)
answer2 = course[11:19]  # "Computer"

# 3. Extract "Science" (starts at position 19, goes to end)
answer3 = course[19:]  # "Science"

# 4. Extract just the first letter "L"
answer4 = course[0]  # "L"

# 5. Extract just the last letter "e"
answer5 = course[-1]  # "e"

#
# Tier 2 - Complete Tasks 6-9
#

# 6. Extract every 2nd character starting from the beginning
answer6 = course[::2]  # "Laigetoptrcec"

# 7. Extract the last 7 characters
answer7 = course[-7:]  # "Science"

# 8. Reverse the entire string
answer8 = course[::-1]  # "ecneicSretupmoCtreCaniveaL"

# 9. Extract "LCC" (first letters of each word - tricky!)
# Positions are 0, 7, 11
answer9 = course[0] + course[7] + course[11]  # "LCC"

#
# Tier 3 - Complete Tasks 10-11
#

# 10. Extract characters in positions 2, 5, 8, 11
answer10 = course[2] + course[5] + course[8] + course[11]  # "agCC"

# 11. Get every third character from the end
answer11 = course[::-3]  # "ecSeo"

#date: 25/09/25
#author: konstantin
#title: zeller's algorithm (program exercise 4)
dd = int(input("day of the month: "))#very difficult
mm = int(input("the month (e.g march = 3 april = 4): "))
y = int(input("the last 2 digits of the year: "))
c = int(input("the last 2 digits of the year: ")) #idk why zeller's algorithm needs this but ok
w = (dd + ((13* (mm + 1)) / 5) + y + (y / 4) + (c / 4) - 2 *(c)) % 7
print("the answer is: ", w)
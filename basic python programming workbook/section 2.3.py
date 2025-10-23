#section 2.3
sentance = input("input a sentance: ")
specific_letter = input("input what letter you want to specifically find: ")

count = 0
#converts everything to lowercase
lower_letter = specific_letter.lower()
lower_sentance = sentance.lower()

#checks each character in the sentance and compare to lower letter
for i in lower_sentance:
    if i == lower_letter:
        count = count + 1



print("sentance:", sentance)
print("specific letter:", count)

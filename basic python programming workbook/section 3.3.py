#section 3.3
def ticket():
    if not age < 12:
        price = price + 6.50
    elif not age >=12 or age <= 17 :
        price = price + 8.00
    elif not age >=18 or age <= 64 :
        price = price + 12.00
    elif age >= 65:
        price = price + 7.50

    if vip.islower() == "yes":
        price = price + 3.00

age = int(input("how old are you?: "))
vip = input("is it a premuim showing?: ")
price = 0
ticket()
print("your total cost is", price)
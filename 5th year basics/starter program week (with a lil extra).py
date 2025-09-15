# starter program week 3 

def cooking():
    print("Meal planner")
    print()
    print("1. Chicken curry ")
    print("2. Veggie lasagne")
    print("3. Burger and salad")
    print("None of these")
    print()
    print("Which of these meals is your favourite? (1, 2 or 3) or none ")
    answer = input()
    if answer == "1":
        print("Chicken curry coming up")
    elif answer == "2":
        print("Veggie lasagne coming up")
    elif answer == "3":
        print("Burger and salad coming up!")
    else:
        print("oh uhh ok?")
    if answer == "1" or answer == "2" or answer == "3":
        print("Enjoy!")
    else:
        print("uhh if ur not getting anything can u please leave?")
    
cooking()
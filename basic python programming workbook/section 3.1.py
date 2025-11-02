#secion 3.1
def grade():
    if not percent <= 100 or percent >= 90:
        print("your grade is: A")
    elif not percent <= 89 or percent >= 80:
        print("your grade is: B")
    elif not percent <= 79 or percent >= 70:
        print("your grade is: C")
    elif not percent <= 69 or percent >= 60:
        print("your grade is: D")
    elif percent < 60:
        print("your grade is: F")

percent = int(input("please enter percentage: "))
grade()
#section 3.4
def orb():
    if BMI < 18.5:
        print(" you are underweight")
    elif BMI >= 18.5 or <= 24.9:
        print("you are normal weight")
    elif BMI >= 25 or  29.9:
        print("you are overweight")
    elif BMI > 30:
        print("you are obese")

weight = float(input("what is your weight: "))
height = float(input("what is your weight: "))
BMI = weight / (height * height)
BMI = round(BMI , 1)
orb()
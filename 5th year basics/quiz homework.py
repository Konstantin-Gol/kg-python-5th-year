#konstantin quiz
def quiz():
    print("welcome to my quiiiiz!!")
    print("hope you have you brain ready and memory sharp couse the quiz starts now")
    print()
    score = 0
    print("Q1. who did will smith slap at the oscars?")
    print("A. chris rock")
    print("B. joe walker")
    print("C. kenneth branagh")
    answer1 = input()
    if answer1 == "a":
        print("who could forget about that XD")
        score = score + 1
    else:
        print("oof sorry it was actually chris rock")
    print()   
    print("Q2. what is happening n nepal right now?(15/9/2025)")
    print("A. nothing really")
    print("B. a bake off")
    print("C. A RIOT AAAAAAHGHGHG")
    answer2 = input()
    if answer2 == "c":
        print("to be fair it's kinda inspiring")
        score = score + 1
    else:
        print("nope they rioted an burned down parlament")
    print()
    print("Q3. why did i make this quiz?")
    print("A. for the fun of it")
    print("B. it's homework T0T")
    print("C. bragging rights")
    answer3 = input()
    if answer3 == "b":
        print("welcome to the sad truth")
        score = score + 1
    else:
        print("i wish but no it's homework")
    print()
    print("Q4. who created spongebob?")
    print("A. pendleton ward")
    print("B. butch hartman")
    print("C. stephen hillenburg")
    answer4 = input()
    if answer4 == "c":
        print("rip king fly high")
        score = score + 1
    else:
        print("nuh uh it was stephen hillenburg")
    print()    
    print("Q5. what programming language is this made on?")
    print("A. python")
    print("B. java")
    print("C. rust")
    answer5 = input()
    if answer5 == "a":
        print("you are very much correct")
        score = score + 1
    else:
        print("should've gone to specsavers")
    print()
    print("ok your score is", score)
    if score > 3:
         print("congrats you did good")
    elif score < 3:
        print("congrats you suck")
    elif score == 3:
        print("congrats you were ok")
    print("bye bye")
    
quiz()
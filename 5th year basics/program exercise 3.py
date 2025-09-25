#date: 25/09/25
#author: konstantin
#title: fahrenheit to centigrade program (program exercise 3)
f = float(input("fahrenheit temperature to convert: "))
c = (f - 32) * 0.56 #python uses bimdas
c = round(c,4) #make sure to put the c = or it won't change
print("the centigrade is:", c) #all done :D
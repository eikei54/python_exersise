#Question 13
#Level 2
#
#Question:
#Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3
#
#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.

string_ = input()
d={"LETTERS":0, "DIGITS":0}

#for car_ in string_[:]:
for car_ in string_:
    #print(car_, type(car_))
    if car_.isalpha():
        d["LETTERS"] += 1
    elif car_.isdigit():
        d["DIGITS"] += 1
    else:
        pass

print("LETTERS:",d["LETTERS"],"DIGITS:",d["DIGITS"] )

#Question 14
#Level 2
#
#Question:
#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#Suppose the following input is supplied to the program:
#Hello world!
#Then, the output should be:
#UPPER CASE 1
#LOWER CASE 9
#
#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.

d={"UP":0, "LO":0}
s=input()
for c in s:
    if c.isupper():
        d["UP"] += 1
    elif c.islower():
        d["LO"] += 1
    else:
        pass
print(d["UP"], d["LO"])






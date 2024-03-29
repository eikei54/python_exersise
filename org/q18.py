
#Question 18
#Level 3
#
#Question:
#A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
#Following are the criteria for checking the password:
#1. At least 1 letter between [a-z]
#2. At least 1 number between [0-9]
#1. At least 1 letter between [A-Z]
#3. At least 1 character from [$#@]
#4. Minimum length of transaction password: 6
#5. Maximum length of transaction password: 12
#Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
#Example
#If the following passwords are given as input to the program:
#ABd1234@1,a F1#,2w3E*,2We3345
#Then, the output of the program should be:
#ABd1234@1
#
#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.

import re

MAX_LEN = int(12)
MIN_LEN = int(6)

item = [x for x in input().split(',')]
password = []
#print(item)

for _p in item:
    if len(_p) > MAX_LEN or len(_p) < MIN_LEN:
      #print(_p, "length is not match")
        continue
    else:
        pass
    if not re.match(".+[a-z]+", _p):
        #print(_p, "not include [a-z]")
        continue
    elif not re.match(".+[0-9]+", _p):
        #print(_p, "not include [0-9]")
        continue
    elif not re.match(".+[A-Z]+", _p):
        #print(_p, "not include [A-Z]")
        continue
    elif not re.match(".+[$#@]+", _p):
        #print(_p, "not include [$#@]")
        continue
    else:
        pass

    password.append(_p)


print(','.join(password))



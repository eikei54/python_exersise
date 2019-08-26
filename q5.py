
#Question 5
#Level 1
#
#Question:
#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.
#
#Hints:
#Use __init__ method to construct some parameters

class Totsuka():
    count = 0
    def __init__(self, name):
        Totsuka.count += 1
        self.name = name
    def getString(self):
        print("getString ", end="")
        return self.name
    def printString(self):
        print("printString", self.name)
    @classmethod
    def printNumInstances(cls):
        print("Totsuka has", cls.count, "instances.")

yabe = Totsuka("VeruTotsuka")
Totsuka.printNumInstances()
yabe.printString()
print(yabe.getString())

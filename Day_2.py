# Question 4:

# Write a program which accepts a sequence of comma-separated numbers from console 
# and generate a list and a tuple which contains every number.

# Solution:

num=input().split(",") # Read input and split them with comma
print(num) # return list
print(tuple(num)) # return tuple


# Question 5:

# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.

# Solution:

class string:
    def __init__(self):
        self.word=""
    def getString(self):
        self.word=input()
    def printString(self):
        print(self.word.upper())

strObj=string()
strObj.getString()
strObj.printString()


# Question 6:

# Write a program that calculates and prints the value according to the given formula:

# Q = Square root of [(2 * C * D)/H]

# Following are the fixed values of C and H:

# C is 50. H is 30.

# D is the variable whose values should be input to your program in a comma-separated sequence.

import math

C,H=50,30

def calc(D):
    return (math.sqrt(2*C*D)/H)

D=input().split(",")
num=[str(round(calc(int(i)))) for i in D]
print(",".join(num))


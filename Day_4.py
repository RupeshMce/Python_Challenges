# Question :10
# A robot moves in a plane starting from the original point (0,0). 
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps

import math

x,y=0,0

while True:
    moves=input().split()
    if not moves:
        break
    if moves[0]=="UP":
        x=x-int(moves[1])
    if moves[0]=="DOWN":
        x=x+int(moves[1])
    if moves[0]=="LEFT":
        y=y+int(moves[1])
    if moves[0]=="RIGHT":
        y=y-int(moves[1])
    else:
        pass
print(x,y)
distance=round(math.sqrt(x**2 + y**2)) 
print("Distance : ",distance)

# Question:11
# Write a program to compute the frequency of the words from the input

string= input()
string=string.split(" ")
word =sorted(set(string))
#print(word)
for i in word:
    print("{}:{}".format(i,string.count(i)))

# Question :12
# Write a program which can map() to make a list whose elements
# are square of elements in [1,2,3,4,5,6,7,8,9,10].

lis=list(range(1,11))
print(list(map(lambda x:x**2,lis))) 
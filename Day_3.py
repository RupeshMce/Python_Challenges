
# Question 7:

# Write a program that accepts a sentence and calculate the number of upper case 
# letters and lower case letters.

word="Hello World"

upper=sum(1 for i in word if i.isupper())
lower=sum(1 for i in word if i.islower())

print("Upper Case {} \nLower Case {}".format(upper,lower))

#Question 8:

# Use a list comprehension to square each odd number in a list.

print(",".join([str(int(i)*int(i)) for i in input().split(",") if (int(i)%2)!=0]))

# Question 9:

# You are required to write a program to sort the (name, age, score) tuples by
# ascending order where name is string, age and score are numbers
# The sort criteria is:
# 1: Sort based on name
# 2: Then sort based on age
# 3: Then sort by score
# The priority is that name > age > score.

from operator import itemgetter, attrgetter

l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print (sorted(l, key=itemgetter(0,1,2)))  # itemgetter to enable multiple sort keys.
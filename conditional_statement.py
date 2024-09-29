#where we have associated with condition than we use conditional statement
#there are three types of conditional statement in python
# if,else , elif

'''
 syntax
 if condition:
 elif condition:
 else
'''

#age program to demonstrate the conditional statement

age=int(input("enter the age of the person:"))
if age>18:
    print("Eligible for vote")
else:
    print("not eligible to vote")

light=input("Enter the light ")
if(light=="red"):
    print("please stop")
elif(light=="yellow"):
    print("Be Ready")
else:
    print("Go")
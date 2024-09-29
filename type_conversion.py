#type conversion and type casting
#type conversion :- when python automaticaly convert the type of the variable
#type casting:- when we forcefully convert the type of veriable

#type conversion
a=9+7.9
print(a)
print(type(a)) #implicit conversion

a=8.9
b="45"
print(a+b) #error does not concatinate string with float
c=int(b) #manually conversion of float into string
print(a+c)
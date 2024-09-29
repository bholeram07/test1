#list :- list is mutable data type in python , always coma seperated
#collection of different types of datatypes in python
l=[1,33,2,'bhole','ram',33.2]
#indexing in the list
print(l[0])
print(l[3])
#to get more than one value
print(l[0:5]) #not included 5
print(l[2::2])

#slicing from the reverse
print(l[-1: :-1])

#iteration of the list 
new_list=[10,20,30,40,50,60]
#length of the list
length=len(new_list)
for i in range(length):
    print(new_list[i])
#second method
for i in new_list:
    print(i)
#from reverse
for i in range(length-1,-1,-1):
    print(new_list[i])

#insert the element in the list

#insert take 2 argument first is position and 2 is value
l.insert(0,90) #(position,value)
print(l)

#append means insert the value in the last of the list
l.append(9)
print(l)
l.append([9,70])
print(l)

#extends works on the value
l.extend([9,30])
print(l)


#delete the element form list
#del need index del deletes the value on index and does not return value
del(new_list[1])
print(new_list)
#pop is same as delete but it return the value that it deleted
new_list.pop(0)
print(new_list)

#remove delete with value
new_list.remove(40)
print(new_list)

#clear delete the whole list
new_list.clear()
print(new_list)


#list comprehension
#list comprehension is the elegant way to define and create a list on the  based
#of the existing list
#more faster than normal function 
# my_list=[]
# for a in range(1,101):
#     my_list.append(a)
# print(my_list)

#list comprehension
my_list=[a for a in range(0,101) if a%2==0]
print(my_list)

#more list function
#count, max,min,sort ,reverse
print(max(my_list))
print(min(my_list))
my_list.sort()
my_list.reverse()
print(my_list)


t="welcome to our world"
l=t.split()
print(l)

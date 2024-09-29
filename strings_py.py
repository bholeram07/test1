#strings are the sequence of the character
str="hii i am bholeram from gkmit"
# string functions
#for the length of the str
print(len(str))
#string concatination
str2=str+"and from geetanjali"
print(str2)
#string is immutable means we can not modify the string value
print(str[0])
print(str[(len(str))-1])
# str[0]="b" #wrong

#string slicing
print(str[0:8]) #does not include ending index
print(str[4:len(str)])
print(str[:])
print(str[:7]) #automatically start from 0 index
print(str[1:]) #automatically reach to the ending index

#negative indexing and slicing
print("from backward")
print(str2[ -7:-1])

#find,replace ,capitalize and count
print(str2[-1::-1])

#for loop iteration of string
for i in str:
    print(i)

#isalpha :- to check all the alphabets in the string
#isdigit :- to check that sting contains all the digit
#isalnum :- to check both the numbers and alphabet in the string

#chr and ord pass ascii value and return the string
print(chr(65))
print(ord('a'))
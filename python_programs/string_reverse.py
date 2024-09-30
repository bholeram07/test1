# name=input("Enter the name of student")
# rev_string=""
# for char in name:
#     rev_string=char+rev_string
# print(rev_string)
# rev_string=name[::-1]
# print(rev_string)


#print prime number
n1=int(input("enter the number you want to check"))
for i in range (2,n1+1):
    if i%n1==0:
        print("This is not a prime number ")
        break
else:
    print("This is Prime Number ")

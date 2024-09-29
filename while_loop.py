#while loop totaly depends on the condition
#syntax while condition:
#program to print even number in reverse manner
n=int(input("enter the number you want to sum natural number "))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print(sum)

#program to print the sum of the odd number 
n_odd=int(input("enter the number you want to print the sum"))
i=0
sum=0
while i<n_odd:
    sum=sum+((2*i)+1)
    i=i+1
print(sum)

#program to print the sum of even number
n_even=int(input("enter the range you want to print the sum of even number "))
i=1
sum=0
while i<=n_even:
    sum=sum+2*i
    i=i+1
print(sum)
try:
    age=int(input("enter your age"))
    if(age<0):
        raise ValueError
    print("Your age is :- ",age)
except ValueError:
    print("Enter the valid age")


class FiveDevisionError(Exception):
    pass


try:
    n1=int(input("enter the number 1"))
    n2=int(input("Enter the number 2"))
    if n2==5:
        raise FiveDevisionError("Can not devide by 5")
    div=n1/n2
    print("The devision is ",div)
except (FiveDevisionError,ZeroDivisionError) as var:
    print(var)
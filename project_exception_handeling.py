import time

class BalanceInsufficientError(Exception):
    pass

class AttemptExceptionError(Exception):
    pass

attempt=1

def withdraw():
    global attempt
    saved_pin=7890
    balance=50000
    pin=int(input("Enter the Pin"))
    if saved_pin==pin:
            try:
                amt=float(input("Enter the amount to withdraw"))
                temp_balance=balance-amt
                if  temp_balance<1000:
                  raise BalanceInsufficientError("Balance Ensufficient")
                balance=temp_balance
                print("money detected and remaining balance ",balance)
            except BalanceInsufficientError as var:
                print(var)
    else:
        ans=input("Do you Want to Continue Again (y/n)")
        if ans.lower()=='y':
            attempt+=1
            try:
                if attempt==4:
                    raise AttemptExceptionError("Too many attempt your account is blocked")
                
            except AttemptExceptionError as var:
                print(var)
                time.sleep(3600)
            else:
                withdraw()
        else:
            print("Thankyou!!")
            return

withdraw()

        


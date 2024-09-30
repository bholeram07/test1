#zero devision error
'''
  python has 4 exceptions
  1. try (execute)
  2. except(if any error than execute)
  3. else (if true than execute)
  4. finally (always execute)
'''

#by class_object
a=int(input("Enter the number 1 "))
b=int(input("Enter the number 2 "))

try:
    div=a/b
    print(div)
except:
    print("Zero Devision Error")
else:
    print("Successfully executed")
finally:
    print("Always Executed")
                                     

    
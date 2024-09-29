#encapsulation means you can not directly access the private methods and variable of the class
''' Encapsulation hides some important details and ahows only necessary information
    __ is the method to declare any variable or method to declare private
    we can access them by calling in constructor
'''
class student:
    __name="bholeram" #private member
    def __init__(self):
        print(self.__name) #access private member of the class
        self.__display()#access private method of the class


    def __display(self):
        print("my name is bholeram")


student_obj=student()
# student_obj.__display() #error 
# print(student_obj.__name) --> not accessible
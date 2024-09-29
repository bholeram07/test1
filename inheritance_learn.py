'''#when the all properteis of the parent class is acquired by child class 
than this called the inhearitance
 In python there was three type of inheritance 
 1. Single (Base --> derived)
 2. Multilevel (Base --> derived1-->derived2)
 3. Multiple (Bade,base2->Derived)
 
'''
#Single inheritance
class student:
    roll_no=None
    def set(self,roll_no1):
        self.roll_no=roll_no1
    def display(self):
        print(self.roll_no)

class result(student):
    marks=None
    def __init__(self, marks):
        self.marks=marks
    def result_display(self):
        print(f"the student whose roll no {self.roll_no} has got marks{self.marks}")

result_obj=result(120)
result_obj.set(121)
result_obj.display()
result_obj.result_display()    
#self is used as the first argument in the function
#self refers to the instance of class itself
#self helps in disinguish between the local variable and class variable
#we can access the class variable only with the help of self
class student:
    name="bholeram"
    roll_no=None
    def set_roll_no(self,roll_no1):
        self.roll_no=roll_no1
    def display(self):
        marks=121
        print(f"the student {self.name} has roll no {self.roll_no} has marks {marks}")
student_obj=student()
student_obj.set_roll_no(191)
student_obj.display()

     
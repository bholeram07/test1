class student:
    roll_no=None
    def __init__(self,rollno1):
        self.roll_no=rollno1
    def display(self):
        print(self.roll_no)

obj_student=student(102)
obj_student.display()

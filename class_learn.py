class student:
    roll_no=[]
    marks=[]
    def get(self):
        count=int(input("enter the number of student you eant to enter:"))
        for i in range(1,count+1):
            ele=int(input(f"enter the roll no. of {i}:-"))
            marks=int(input(f"enter the marks of the student {i}:-"))
            self.roll_no.append(ele)
            self.marks.append(marks)
        
    def display(self):
        print(self.roll_no)
        print(self.marks)

class result(student):
    def display(self):
        return super().display() #method overloading 

result1=result()
result1.get()
result1.display()
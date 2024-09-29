class A:
    def display(self):
        print("This is Class A")

class B:
    def displayB(self):
        print("This is Class B")

class C(A,B):
    def displayC(self):
        return super().display()
    
c_obj=C()
c_obj.display()
c_obj.displayB()
c_obj.displayC()
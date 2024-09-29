class A:
    def displayA(self):
        print("This is class A")



class B(A):
    def displayB(self):
        print("this is Class B")

class C(B):
    def displayC(self):
        print("This is Class C")

C_obj=C()
C_obj.displayA()
C_obj.displayB()
C_obj.displayC()
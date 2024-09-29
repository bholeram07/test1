class A:
    def __init__(self):
        self.a=" "
    def set(self,name):
        self.a=name
    def get(self):
        print(self.a)

obj_A=A()
obj_A.set('bhole')
obj_A.get()
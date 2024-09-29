class BikeShop:
    def __init__(self,stock):
        self.stock=stock
    def display_details(self):
        print(f"Total BIkes available are {self.stock}")
    def Rent_for_bike(self,q):
        if(q<0):
            print("Please Enter Positive Value ")
        elif(q>self.stock):
            print("Out of stock")
        else:
            print(f"Bike Rented {q}")
            print(f"For Total Price {q*500}")
            self.stock=self.stock-q
            print("Now available Bikes are: ",self.stock)

while True:
    obj_bikeshop=BikeShop(20)
    uchoice=int(input(''' Enter your choice
                      1. Display Total Stock
                      2. Rent For Bike
                      3. exit
        \n'''))
    if uchoice==1:
        obj_bikeshop.display_details() 
    if uchoice==2:
        obj_bikeshop.Rent_for_bike(10)
    else:
        break
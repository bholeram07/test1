import random
while True:
    random_number=random.randint(1,9)
    user_n=input("Enter the number: ")
    user_key=input("Enter the key or g: ")
    if not user_n.isdigit():
        continue
    if(int(user_n)<0 and int(user_n)>9):
        continue
    if(user_key=='g'):
        print("Congrats! the key is matched")
        break
    if(random_number==int(user_n)):
        print("Congrats! the random number is matched ")
        break
    else:
        continue
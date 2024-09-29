#rock scissor game
#rock vs paper = paper wins
#rock vs scissor= rock wins
#paper vs scissor =scissor wins

import random

countc=0
countu=0
while(True):
    list=['rock','paper','scissor']
    computer_choice=random.choice(list)
    game=int(input('''Press Key for Game Start -->
                   1. YES
                   2. NO
                   \n'''))
    if(game==1):
        for i in range(1,6):
            user_choice=(input(''' Enter your choice:-
            1. rock
            2. scissor
            3. paper \n'''))
            if user_choice == computer_choice:
              print("Match Draw ,Both choices are same")
            elif (user_choice=='rock' and computer_choice=='scissor') or (user_choice=='scissor' and computer_choice=='paper') or (user_choice=='paper' and computer_choice=='rock'):
              print("you Win")
              print("Your choice:- ",user_choice)
              print("Computers Choice:- ",computer_choice)
              countu+=1
            else:
              print("Computer Win !!")
              print("Your choice:- ",user_choice)
              print("Computers Choice:- ",computer_choice)
              countc+=1    
        if(user_choice==computer_choice):
           print("Match Draw") 
           print("User Count-",countu)
           print("Computer Coice:-",countc) 
        elif countu>countc:
           print("Congrats! YOU WIN")
           print("User Count:-",countu)
           print("Computer Count:-",countc)  
        else:
           print("Sorry!! Computer Win")
           print("User Count:-",countu)
           print("Computer Count:-",countc)  
    else:
        break

    

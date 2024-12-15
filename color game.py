"""
Welcome to the color game>>>
please enter the name for score board

1> start game
2> exit

if 1
please enter the color: redasddfa
 validate the color if the given color is not present in the
 list then tell user you have entered invalid color

 if color is validated then
 match it with machine generated color
 if matching then display the message like
 you wom the game
 number of attempts : 1
 total number of attempts: 5

 if not matching then display the message:

 your guess was wrong please try again
 number of attempts left: 04

 once after completing the game till 5th attempts tell user
 1> see score board
 2> play again
 3> exit

 if he  choose 1 then:
 number of game won:01
 number of game loose:01
 name of the player: abc
"""

import random
choice=1
game_won=0
game_lose=0
color=['red','green','yellow','black','blue','white']
score=0

def check_color(user_color):
    return user_color in color

print("Welcome to the color game>>> \nplease enter the name for score board\n1> start game\n2> exit")
choice=int(input("Enter your choice:"))

while (choice==1):
    life=5
    while (life>0):
        print("CHOOSE COLOR from RED, GREEN, BLUE, BLACK, WHITE, YELLOW\n")
        comp_color=random.choice(color)
        user_color=input("Enter your color:")

        if check_color(user_color.lower()):

            if user_color.lower()==comp_color:
                print("You Won")
                game_won+=1
                life-=1
           
            else:
                print("You lost")
                game_lose+=1
                life-=1
        
        print("Number of attempts left: ",life)

    
    print("\n1> Play Again\n2> Score Board\n3> Exit")
    choice=int(input("Enter your choice:"))
    if choice==2:
        print ("Number of games you won:",game_won,"\nNumber of games you lost:",game_lose,'\n')
        print("\n1> Play Again\n2> Score Board\n3> Exit")
        choice=int(input("Enter your choice:"))
        
    
    

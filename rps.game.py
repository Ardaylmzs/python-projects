# rock paper and scissors game
scissors ='''
          ,/'
  (_).  ,/'
   _  \::
  (_)'  `\.
           `\.
VK'''
paper ='''    
                     _.-._
                    | | | |_
                    | | | | |
                    | | | | |
                  _ |  '-._ |
                  \`\`-.'-._;
                   \    '   |
                    \  .`  /
              jgs    |    |
'''
rock ='''  
             .----.-----.-----.-----.
            /      \     \     \     \ 
           |  \/    |     |   __L_____L__
           |   |    |     |  (           
           |    \___/    /    \______/    |
           |        \___/\___/\___/       |
            \      \     /               /
             |                        __/
              \_                   __/
               |        |         |
               |                  |
               |                  |
                  _______            
                           
 '''
user_choice = int(input("what do you choose type ? type 0 for rock , 1 for paper , 2 for scissors.\n"))
import random

computer_choice = random.randint(0,2)

game_images = [rock,paper,scissors]

if 0 <= user_choice <= 2:
    print(game_images[user_choice])
    print("Computer chose:")
    print(game_images[computer_choice])

print(f"computer chose {computer_choice}")

if user_choice >= 3 or user_choice < 0:
    print("you typed an invalid number.You lose!")
if user_choice == computer_choice:
    print("it's a draw")
elif user_choice == 0 and computer_choice == 2 :
    print("you win!")
elif computer_choice == 0 and user_choice == 2 :
    print("you lose!")
elif user_choice > computer_choice :
    print("you wins!")
else :
    print("you lose!")




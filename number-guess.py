import random
def guess_number():
    print("welcome to the guess number challange")
    print("please you try to guess the number between 1 and 100")
    random_number = list(range(1,101))
    should_continue = True
    answer = int(random.choice(random_number))
    while should_continue:
        choice = input("how do you want to select the part of game ? hard or easy ; type 'e' for easy or 'h' for hard:")
        guess = int(input("please enter a number :"))
        if choice == 'h':
            for hardness in range(1,5):
                game_over = hardness
                if guess == answer:
                    print("*****congratulations!*****")
                    print(f"you guessed the correct number {guess}")
                    should_continue = False
                    break
                if guess < answer and guess != answer:
                    print("try again , unfortunately , you guessed incorrect number!!")
                    print("too low")
                    guess = int(input("please enter a number :"))
                elif guess > answer and guess != answer:
                    print("try again , unfortunately you guessed incorrect number!!")
                    print("too high")
                    guess = int(input("please enter a number :"))
                if game_over == 4:
                    should_continue = False
                    print("you lose!!!")
                    print(f" answer is {answer}")
                    break
        if choice == 'e':
            for easy in range(1,10):
                game_over_1 = easy
                if guess == answer:
                    print("you guessed correctly")
                    should_continue = False
                    break
                if guess < answer :
                    print("try again , unfortunately , you guessed incorrect number!!")
                    print("too low")
                    guess = int(input("please enter a number :"))
                elif guess > answer:
                    print("try again , unfortunately you guessed incorrect number!!")
                    print("too high")
                    guess = int(input("please enter a number :"))
                if game_over_1 == 9:
                    should_continue = False
                    print("you lose!!!")
                    print(f" answer is {answer}")
                    break
guess_number()




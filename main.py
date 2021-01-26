import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("there is currently no high score, its yours for the taking")
    else:
        print("the current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1,10))
    print("hello traveller! welcome to the game of guesses!")
    player_name = input("what is your name?")
    wanna_play = input("hi {} would you like to play the game (enter y/n)".format(player_name))
    attempts = 0
    show_score()
    while wanna_play.lower() == "y" :
        try:
            guess = input("pick a number between 1 to 10")
            if int(guess)<1 or int(guess) > 10:
                raise ValueError("guess the number within the range")
            if int(guess) == random_number:
                print("nice you got it!")
                attempts += 1
                attempts_list.append(attempts)
                print("It took you {} attempts".format(attempts))
                play_again = input("Would you like to play again? (Enter Yes/No) ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 10))
                if play_again.lower() == "no":
                    print("That's cool, have a good one!")
                    break
            elif int(guess) > random_number:
                print("It's lower")
                attempts += 1
            elif int(guess) < random_number:
                print("It's higher")
                attempts += 1
        except ValueError as err:
                print("Oh no!, that is not a valid value. Try again...")
                print("({})".format(err))
    else:
        print("That's cool, have a good one!")

if __name__ == '__main__':
   start_game()

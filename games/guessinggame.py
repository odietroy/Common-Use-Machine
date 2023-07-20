import random


def guessinggame():
    prompted = False
    gameswon = 0
    playagain = 'n'
    secretnumber = random.randint(1, 10)

    print("Try to guess the random number from 1 to 10!")

    attempts = 0
    while True:
        while attempts < 3:
            guess = input("Guess: ")
            attempts += 1
            if guess == str(secretnumber):
                gameswon += 1
                print(f"You guessed the number! It was {str(secretnumber)}.")
                print(f"You have won {gameswon} games")
                playagain = input("Would you like to play again? (Y/N) ")
                prompted = True
                if playagain.lower() == 'y':
                    attempts = 0
                    secretnumber = random.randint(1, 11)
                if playagain.lower() == 'n':
                    attempts = 3

            elif guess == 'debug':  # debug for debugging the different functions
                print(str(secretnumber))
        if not prompted:
            playagain = input(
                f"You failed after winning a total of {gameswon} games. Would you like to play again? (Y/N) ")
        if playagain.lower() == 'n':
            print("Goodbye!")
            break
        if playagain.lower() == 'y':
            attempts = 0
            secretnumber = random.randint(1, 11)

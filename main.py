from time import sleep
from guess import Guess


def main():
    game = Guess()
    play = False
    
    while not play:

        rawInput = input(
        '''
        ========================================
        |              WELCOME                 |
        |                                      |
        |         I'll be your guesser         |
        | Think of a number between 0 and 1000 |
        |        Type 'play' when ready        |
        ========================================
        \n> '''
        )

        if rawInput == "play":
            play = True
        else:
            rawInput = print("Incorrect.")


    
    print("Let's begin")
    sleep(2)


    correct = False

    while not correct:
        if game.makeAGuess() == 1: # INSTA WIN
            print(f"Your number HAS to be {game.minPossible}.")
            correct = True
            pass
        else:
            case = checkGuess()
            if case == "H":
                game.tooLow()
            elif case == "L":
                game.tooHigh()
            elif case == "C":
                game.celebrate()
                correct = True

    print("Thank you for playing.")
    return



def checkGuess():
    while True:
        rawInput = input("Is your number, (H)igher, (L)ower, (C)orrect?")

        if rawInput == "H": #HIGHER
            return "H"
        elif rawInput == "L": #LOWER
            return "L"
        elif rawInput == "C": #CORRECT
            return "C"
        else:
            print("Incorrect.")
            rawInput = input("> ")



if __name__ == '__main__':
    main()
from random import randint
from time import sleep

class Guess:

    def __init__(self):
        self.currentGuess = 0
        self.minPossible = 0
        self.maxPossible = 1000

        self.banterList = [
            "banter 1",
            "banter 2",
            "banter 3",
            "banter 4",
            "banter 5"
        ]

        self.curseList = [
            "curse 1",
            "curse 2",
            "curse 3",
            "curse 4",
            "curse 5"
        ]

        self.celebrateList = [
            "celebrate 1",
            "celebrate 2",
            "celebrate 3",
            "celebrate 4",
            "celebrate 5"
        ]
    

    def banter(self):
        print(self.banterList[randint(0, 4)])
        sleep(randint(1, 3))

    def curse(self):
        print(self.curseList[randint(0, 4)])
        sleep(randint(1, 3))

    def celebrate(self):
        print(self.celebrateList[randint(0, 4)])
        sleep(randint(1, 3))

    def tooHigh(self):
        if self.currentGuess <= self.maxPossible:
            self.maxPossible = self.currentGuess -1

    def tooLow(self):
        if self.currentGuess >= self.minPossible:
            self.minPossible = self.currentGuess +1


    def makeAGuess(self):
        self.banter()

        if self.minPossible == self.maxPossible:
            return 1
        else:
            self.currentGuess = randint(self.minPossible, self.maxPossible)
            print(f"I'm thinking of {self.currentGuess}")
            return 0



def main():

    game = Guess()

    print("Welcome \nI'll be your guesser for the game \nThink of a number between 0 and 1000\n\n")

    
    play = False
    while not play:
        rawInput = input("Type 'play' when ready!")
        if rawInput == "play":
            play = True
        else:
            rawInput = print("Incorrect.")


    
    print("Let's begin")
    sleep(2)


    correct = False

    while not correct:

        if game.makeAGuess() == 1: # INSTA WIN
            print(f"Your number HAS to be {game.currentGuess}.")
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

        print(game.minPossible)
        print(game.maxPossible)

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
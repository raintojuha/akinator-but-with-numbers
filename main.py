class Guess:

    def __init__(self, target):
        self.currentGuess = 0
        self.minPossible = 0
        self.maxPossible = 0
        self.target = target

class Message:

    def __init__(self):
        self.tooLarge = "Too large to handle!"
        self.negative = "Stay positive. Your number I mean!"
        self.zero = "Okay. I guess that's a number."
        self.notAnuber = "Do you know what a number is"




def takeUserInput(question):
    msg = Message()
    raw = input(f"{question}: ")
    goodInput = False
    while goodInput == False:
        isInt = True
        try:
            int(raw)
        except ValueError:
            print(msg.notAnuber)
            isInt = False

        if isInt:
            if int(raw) < 0:
                print(msg.negative)
                pass
            elif int(raw) > 1000:
                print(msg.tooLarge)
                pass
            else:
                goodInput = True
                if raw == 0:
                    print(msg.zero)
                return raw
        
        raw = input("> ")
            



def main():

    userTarget = takeUserInput("Number please")

    game = Guess(userTarget)
    print(game.currentGuess)
    print(game.minPossible)
    print(game.maxPossible)
    print(game.target)

    

    return


if __name__ == '__main__':
    main()
#Module AssortedMethods.py
def numValid(msg):
    while True:
        try:
            userInput = int(input(msg))
        except ValueError:
            print("Eso no es un numero")
            continue
        else:
            return userInput
        break
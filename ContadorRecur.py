#Module ContadorRecur.py
import AssortedMethods

def countRecur(num):
    print(num)
    if num == 0:
        return "BOOOOOOOOOOOOOOOOOOOM!!!!!!"
    return countRecur(num - 1)

def countRun():
    num = AssortedMethods.numValid("¿Qué número será el inicio del contador?: ")
    print(countRecur(num))
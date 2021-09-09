#Module SumaRecur.py
import AssortedMethods
def sumRecur(lista, n):
    if(len(lista) == 1):
        return lista[0]
    else:
        return lista[0] + sumRecur(lista[1:], n)

def sumRun():
    lista = []
    long = AssortedMethods.numValid("¿De cuántos elementos será la suma?")

    for i in range(len(lista),long):
        lista.append(0)

    for i in range(long):
        lista[i] = AssortedMethods.numValid(f"Ingresa el numero para el {i+1} elemento: ")

    print(sumRecur(lista, len(lista)))

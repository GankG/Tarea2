# Module: Main
import FibonacciRecur
import AssortedMethods
import ListaSplice
import SumaRecur
import ContadorRecur


def ayeNay(msg):
    while True:
        userInput = str(input(msg))
        if len(userInput) > 1:
            print("Por favor solo ingresa Y o N.")
            continue
        elif userInput.lower() == "y":
            return True
            break
        elif userInput.lower() == "n":
            return False
            break
        else:
            print("Por favor ingresa Y o N.")


printer = "\nElige un programa a correr entre los siguientes: \n1.- Fibonacci con Recursividad.\n" \
          "2.- Suma de enteros con recursividad.\n3.- Contador BOOM\n4.- Eliminar elemento de arreglo\n---\n"
picker = int(0)
while True:
    picker = AssortedMethods.numValid(printer)
    if 0 < picker < 5:
        if picker == 1:
            FibonacciRecur.serieRun()
        elif picker == 2:
            SumaRecur.sumRun()
        elif picker == 3:
            ContadorRecur.countRun()
        elif picker == 4:
            ListaSplice.spliceRun()
    else:
        print("\n¡Por favor elige una opción entre 1 y 4!\n")
    if not (ayeNay("¿Quieres continuar ejecutando programas? (Y/N)")):
        break

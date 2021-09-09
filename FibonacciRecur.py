# Module: FibonacciRecur.py
import AssortedMethods
fib = [0, 1]
def serieRecur(num):
    if num > 0 and num <= len(fib):
        return fib[num-1]
    else:
        calc = serieRecur(num-1) + serieRecur(num-2)
        if num > len(fib):
            fib.append(calc)
        return calc

def serieRun():
    num = serieRecur(AssortedMethods.numValid("Ingresa un número para la serie de Fibonacci: "))
    print(fib)

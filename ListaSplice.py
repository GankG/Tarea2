#Module ListaSplice.py
def spliceMid(arr, long):
    if (long % 2) == 0:
        long = (long//2) - 1
        arr = arr[:long-1] + arr[long:]
    else:
        long = long//2
        arr = arr[:long] + arr[long+1:]

    return arr


def spliceRun():
    arr = str(input("Ingresa cualquier cosa, de cualquier longitud: "))
    long = len(arr)
    print(spliceMid(arr, long))

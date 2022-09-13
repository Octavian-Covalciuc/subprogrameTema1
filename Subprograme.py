def putere():
    s = 0
    for i in range(0,9,2):
        s += 0.5**i
    return s

# print(putere())

m = 5
n = 10
def fact(x):
    if x == 0:
        return 1
    return fact(x-1) * x

# print(fact(n)/fact(m)/fact(n-m))

def adunareFractii(x : list, y : list):
    return f'{x[0] * y[-1] + y[0] * x[-1]}/{y[-1] * x[-1]}'

# print(adunareFractii([1,4], [1,2]))

def inmultireaFractii(x : list, y : list):
    return f'{x[0] * y[0]}/{x[-1] * y[-1]}'

# print(inmultireaFractii([1,4], [1,2]))

def creareListaInt(n):
    lst = []
    for i in range(n):
        element = input('Dati un element de tip integer: ')
        try:
            lst.append(int(element))
        except:
            while not element.isnumeric():
                element = input('Mai incercati: ')
            lst.append(int(element))
    return lst

# print(creareListaInt(5))

def creareListaFloat(n):
    lst = []
    for i in range(n):
        element = input('Dati un element de tip float: ')
        try:
            lst.append(float(element))
        except:
            while not element.isdecimal():
                element = input('Mai incercati: ')
            lst.append(float(element))
    return lst

# print(creareListaFloat(5))
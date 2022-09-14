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

print(creareListaFloat(5))

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

print(creareListaInt(5))

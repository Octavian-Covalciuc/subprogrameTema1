def adunareFractii(x : list, y : list):
    return f'{x[0] * y[-1] + y[0] * x[-1]}/{y[-1] * x[-1]}'

print(adunareFractii([1,4], [1,2]))

def inmultireaFractii(x : list, y : list):
    return f'{x[0] * y[0]}/{x[-1] * y[-1]}'

print(inmultireaFractii([1,4], [1,2]))

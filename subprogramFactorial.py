m = int(input('dati m: '))
n = int(input('dati n: '))
if m < n:
    def fact(x):
        if x == 0:
            return 1
        return fact(x-1) * x

    print('Numarul de combinari din {n} elemente cate {m} este {fact(n)/fact(m)/fact(n-m)}')
else:
    print('m trebuie sa fie mai mic ca n')

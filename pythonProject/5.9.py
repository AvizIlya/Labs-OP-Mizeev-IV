# Составить программу вывода разложения бинома Ньютона:
# (a+b)n = C(0,n)an b0 + C(1,n)an-1 b1 + ... + C(n,n)a0bn , где

def fact(m):
    f = 1
    for i in range(1, m + 1):
        f = f * i
    return f


def koef(n, k):
    a = fact(n)
    b = fact(k)
    c = fact(n - k)
    return a // (b * c)


if __name__ == '__main__':
    n = int(input("Введите n:"))
    k = 0
    while k <= n:
        print(koef(n, k), "*a^", n - k, "*b^", k, sep='', end='')
        k = k + 1
        if k <= n:
            print(" + ", end='')

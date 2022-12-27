import time

if __name__ == '__main__':
    max = input('Введите число до которого будет находится число Мерсера:')
    count = 0
    if max.isdigit():
        num = 0
        while count < int(max) and (2 ** int(count) - 1) < int(max):
            count += 1
            num = 2 ** int(count) - 1

            prime = num > 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3)
            i = 5
            d = 2
            while prime and i * i <= num:
                prime = num % i != 0
                i += d
                d = 6 - d
            if prime == True:
                print(num, "Степень - ", count )
            time.sleep(0.2)
    else:
        print('вы ввели некоректное значение')

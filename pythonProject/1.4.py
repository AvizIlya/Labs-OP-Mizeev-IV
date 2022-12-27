if __name__ == '__main__':
    count = input('Введите кол-во натуральных чисел:')
    if count.isdigit():
        print(list(range(1, int(count) + 1, 1)))
    else:
        print('вы ввели некоректное значение')

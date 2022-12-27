# Приняв способ изображения рационального числа в виде записи с двумя
# полями [числитель, знаменатель] целого типа написать программу, позволяющую:
# а) определить, есть ли среди 10 рациональных чисел равные;
# б) вычислить наибольшее из данных рациональных чисел (числа не обязательно
# имеют несократимую форму).
# Для хранения рациональных чисел использовать словарь.

if __name__ == '__main__':
    dictionary = {}
    print('оставте пустую строку для окончания ввода')
    for count in range(100):
        number = input('Введите число в виде bb,aa:')
        if number == '':
            break
        dictionary.update({count+1:number})
    splitting = [int(fraction[0]) / int(fraction[1]) for fraction in dictionary.values()]
    print('Список деления:', splitting)
    if (len(splitting) == len(set(splitting))):
        print("Нет одинаковых дробей")
    else:
        print("Есть одинаковые дроби")
    max_fraction = 4 / 2

    for i in splitting:
        if i > max_fraction:
            max_fraction = i
    print('Самое большая дробь:', max_fraction)

    n = 1
    for i in splitting:
        if i == max_fraction:
            break
        n += 1
    print('Наибольший элемент под номером: ', n)

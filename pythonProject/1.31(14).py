def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    min_sum = input('Введите целое ОТ которого числа k будет находится сумма:')
    max_sum = input('Введите целое число n ДО которого будет находитч сумма:')
    downer_border = input('Введите целое число ОТ которого будет вычеслины все члены ряда:')
    upper_border = input('Введите целое число E ДО которого будет вычеслины все члены ряда:')
    function_result = 0
    k = 0
    fun_sum = 0
    count = 0
    denominator = 0

    if is_int(max_sum) and is_int(min_sum) and max_sum > min_sum:
        while int(min_sum) < int(max_sum):
            denominator = 5 * int(min_sum) * int(min_sum) + (8 * int(min_sum)) - 1
            if (denominator) != 0:
                function_result = ((4 * int(min_sum)) / denominator)
                fun_sum = fun_sum + function_result
                min_sum = int(min_sum) + 1
        print("сумма чисел из данного промежутка:", function_result)
    else:
        print("Введенно не целое число!")
    if is_int(upper_border) and is_int(downer_border) and upper_border > downer_border:
        while int(downer_border) < int(upper_border):
            denominator = 5 * int(downer_border) * int(downer_border) + (8 * int(downer_border)) - 1
            if (denominator) != 0:
                function_result = ((4 * int(downer_border)) / denominator)
                downer_border = int(downer_border) + 1
            print(function_result, end=",")
    else:
        print("Введенно не целое число!")

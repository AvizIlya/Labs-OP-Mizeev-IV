# В порядке убывания напечатать все целые числа из диапазона
# 1..10000, которые представимы в виде n2+2k2, но не представимы
# в виде 7ij+j+3 (n, k, i, j >= 0).
def IsAlpha(check_symdol):
    try:
        int(check_symdol)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    max_volue = input('Введите до скольки искать числа подзодящие под условия задачи:')
    max_count = int(max_volue)
    for count_k in range(max_count):
        for count_n in range(max_count):
            result_function = (max_count - count_n - 1) ** 2 + 2 * (max_count - count_k - 1) ** 2
            # Формулу проверки можно упростить если i=0, то j + 3=любой результат который > 2
            result_chek = result_function - 3
            if result_chek < 0 and result_function > 0:
                print(result_function)

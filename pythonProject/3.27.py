# Если в списке есть отрицательные элементы, найти наибольший из них.
def IsDigit(check_symdol):
    try:
        int(check_symdol)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    array = []
    print('оставте пустую строку ввода для окончания ввода списка')
    for count in range(1, 100):
        array.append(int(input(f'Введите {count} элемент списка:')))
        if array[count - 1] == '':
            array.pop
            break
    print(array)
    i = 0
    index = -1
    while i < len(array):
        if IsDigit(array[i]) == True:
            if int(array[i]) < 0 and index == -1:
                index = i
            elif array[i] < 0 and array[i] > array[index]:
                index = i
                i += 1
    print(index + 1, ':', array[index])

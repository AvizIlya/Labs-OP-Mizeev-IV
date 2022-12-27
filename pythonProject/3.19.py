# Напишите программу, конструирующую список
# из «центральных» элементов трёх заданных списков.
def Split_Symbol(line):
    return [char for char in line]


if __name__ == '__main__':
    print_list = ""
    print('оставте пустую строку для окончания ввода строк')
    for count in range(1, 100):
        line_1 = input(f'Введите {count} строку:')
        if line_1 == '':
            break
        symbol_1 = Split_Symbol(line_1)
        if len(symbol_1) % 2 == 0:
            print_list = print_list + symbol_1[(len(symbol_1) // 2) - 1]
            print_list = print_list + symbol_1[(len(symbol_1) // 2)]
        else:
            print_list = print_list + symbol_1[(len(symbol_1)) // 2]
    print(print_list)

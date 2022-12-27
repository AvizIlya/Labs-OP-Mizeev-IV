# Дан текст, каждый символ которого может быть малой буквой, цифрой
# или одним из знаков «+», «-», «*». Группой букв будем называть такую
# совокупность последовательно расположенных букв, которой непосредственно
# не предшествует и за которой непосредственно не следует буква. Аналогично
# определим группу цифр и группу знаков. Если в данном тексте имеется не
# менее двух групп букв, то каждый знак «+», встречающийся между двумя группами
# букв, заменить цифрой 1, знак «-» заменить цифрой 2, а знак «*» – цифрой 3.
# Иначе оставить текст без изменений.
def Split_Symbol(line):
    return [char for char in line]


def IsAlpha(check_symdol):
    try:
        int(check_symdol)
        return False
    except ValueError:
        return True


if __name__ == '__main__':
    line = input('Введите строку:')
    symbol = Split_Symbol(line)
    for count in range(len(symbol) - 2):
        if IsAlpha(symbol[count]) and IsAlpha(symbol[count + 2]):
            if symbol[count + 1] == "+":
                symbol[count + 1] = 1
            if symbol[count + 1] == "-":
                symbol[count + 1] = 2
            if symbol[count + 1] == "*":
                symbol[count + 1] = 3
    print("".join(map(str, symbol)))

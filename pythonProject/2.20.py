# Из заданного набора слов выбрать все слова, имеющие рифмы
# (рифма определяется по принципу, придуманному Незнайкой:
# два слова рифмуются, если последние слоги у них совпадают,
# например, «палка – селедка»).
if __name__ == '__main__':
    word_1 = input("Введите первое слово: ")
    word_2 = input("Введите второе слово: ")
    for char in word_1:
        if char.isalpha() == False:
            word_1 = ""
    for char in word_2:
        if char.isalpha() == False:
            word_2 = ""
    if (len(word_1) != 0 and len(word_2)) != 0 and word_1[-1] == word_2[-1] and word_1[-2] == word_2[-2]:

        print("они рифмичны ")
    else:
        print("вы ввели не слово!")

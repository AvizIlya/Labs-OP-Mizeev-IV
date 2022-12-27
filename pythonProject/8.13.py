# Дан файл f, компоненты которого являются целыми числами.
# Получить файл g, образованный из файла f исключением повторных
# вхождений одного и того же числа.
import re

if __name__ == '__main__':
    f_txt = open("f.txt", "r+")
    text_f = f_txt.read()
    nums = set(re.findall('-?\d+', text_f))
    g_txt = open("g.txt", "w+")
    lst = []
    for a in nums:
        lst.append(a)
        g_txt.write(a)
        g_txt.write(",")
    g_txt.close()
    g_txt = open('g.txt', 'r+')
    Result = ', '.join(nums)
    print("Исходные числа в файле f: ", text_f)
    print("Числа в файле g: ", Result)
    g_txt.close
    f_txt.close

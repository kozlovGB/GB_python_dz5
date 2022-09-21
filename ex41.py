def coding(list_start):
    count = 1
    res = ''
    for i in range(len(list_start)-1):
        if list_start[i] == list_start[i+1]:
            count += 1
        else:
            res = res + str(count) + list_start[i]
            count = 1
    if (list_start[len(list_start)-2] != list_start[-1] or count>1):
        res = res + str(count) + list_start[-1]
    return res

def decoding(list_start):
    number = ''
    res = ''
    for i in range(len(list_start)):
        if not list_start[i].isalpha():#Метод строки str.isalpha() возвращает True, если все символы в строке str являются буквенными и есть хотя бы один символ (строка не пустая и не состоит из одного пробела), в противном случае False.
            number += list_start[i]
        else:
            res = res + list_start[i] * int(number)
            number = ''
    return res


a = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(a)}")
print(f"Текст после дешифровки: {decoding(coding(a))}")
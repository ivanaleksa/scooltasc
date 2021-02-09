# функция кодирования и декодирования
def code_text(napr, rot, lng, txt):
    if lng == 'rus':
        abc = rus_lower_alphabet
        ABC = rus_upper_alphabet
        mosch = 32
    elif lng == 'en':
        abc = en_lower_alphabet
        ABC = en_upper_alphabet
        mosch = 26
    result = ''
    if napr == 1:
        for i in txt:
            if i.isalpha() and i.islower():
                result += abc[(abc.find(i) + rot) % mosch]
            elif i.isalpha() and i.isupper():
                result += ABC[(ABC.find(i) + rot) % mosch]
            else:
                result += i
    if napr == 2:
        for i in txt:
            if i.isalpha() and i.islower():
                result += abc[(abc.find(i) - rot) % mosch]
            elif i.isalpha() and i.isupper():
                result += ABC[(ABC.find(i) - rot) % mosch]
            else:
                result += i
    return result


# функция проверки текста на соответствие языку
def proverka_text(txt, lng):
    for i in txt:
        if lng == 'rus' and i.isalpha() and i not in rus_lower_alphabet and i not in rus_upper_alphabet:
            return False
        elif lng == 'en' and i.isalpha() and i not in en_lower_alphabet and i not in en_upper_alphabet:
            return False
    else:
        return True


# основная программа, ввод данных с проверкой на корректность
en_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
en_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
print('Вас приветствует программа "Шифр Цезаря".')
while True:
    print('''Сделайте выбор:
    >> 1 - если Вы хотите зашифровать сообщение
    >> 2 - если Вы хотите расшифровать сообщение''')
    way = input('>>')
    if way != '1' and way != '2':
        print('Вы ошиблись при вводе, попробуйте еще раз.')
    else:
        way = int(way)
        break
while True:
    print('''Выберите язык сообщения:
    >> rus - русский
    >> en - английский''')
    lang = input('>>')
    if lang != 'rus' and lang != 'en':
        print('Вы ошиблись при вводе, попробуйте еще раз.')
    else:
        break
while True:
    sdvig = input('Введите шаг сдвига:\n>>')
    if not sdvig.isdigit():
        print('Вы ошиблись при вводе, попробуйте еще раз.')
    else:
        sdvig = int(sdvig)
        break
while True:
    text = input('Введите сообщение\n>>')
    if proverka_text(text, lang):
        break
    else:
        print('Язык сообщения не соответствует выбранному языку. Попробуйте еще раз.')

# вывод результата
for elem in range(0,26):
    print(code_text(way, elem, lang, text))

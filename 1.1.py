# 1.1
# print('Введите имя')
# name = input()
# print('Введите фамилию')
# surname = input()
# print('Введите любимое животное')
# animal = input()
# print('Введите знак зодиака')
# zodiac = input()
# print('Индивидуальный гороскоп для пользователя', name, surname)
# print('Кем вы были в прошлой жизни:', animal)
# print('Ваш знак зодиака -', zodiac, ',поэтому вы - тонко чувствующая натура.')


# 1.2
# print('Памятка для начинающего программиста:')
# print('1 бит - минимальная единица количества информации.')
# print('1 байт = 8 бит.')
# print('1 Килобит = 1024 бита.')
# print('1 Килобайт = 1024 байта.')
# Kb = 1024*8;
# print('1 Килобайт =', Kb, 'бит.')


# 1.3
# print('Введите 3 строки')
# Line1 = input()
# Line2 = input()
# Line3 = input()
# print(Line3, Line2, Line1)


# 2.1
# print('Вы находитесь в пещере на развилке. Вы можете пойти НАЛЕВО, НАПРАВО или ПРЯМО.')
# print('Выберите куда пойти: одно из слов, указанных заглавными буквами')')
# way = input()
# if way == 'налево':
#     print('Вы направились налево. Вы выберете ЛЕВУЮ или ПРАВУЮ дверь?')
#     way1 = input()
#     if way1 == 'правую':
#         print('Вы смело открыли правую дверь.')
#         print('Но за ней вас подстерегала гигантская подземная жаба, которая проглотила вас целиком!')
#     else:
#         print('Вы открыли левую дверь. Вы выбрались из лабиринта!')
# else:
#     if way == 'направо':
#         print('Вы направились направо. Вы оказались взаперти. Пути назад нет. Время умирать')
#     else:
#         print('Вау! Вы сразу нашли путь наружу! Поздравляю! Вы живы!')
#


# 2.2
# print('Введите желаемый логин')
# login = input()
# print('Введите резервный адрес электронной почты')
# backup = input()
# if '@' in login:
#     print('Некорректный логин')
# elif '@' not in backup:
#     print('Некорретный адрес')
# else:
#     print('OK')

# 2.3
# print('Какое у Вас настроение?')
# answer = input()
# if 'хорошее' in answer or 'прекрасное' in answer or 'отличное' in answer:
#     print('Замечательно, у меня тоже все хорошо')
# elif 'плохое' in answer or 'не очень' in answer or 'ужасное' in answer:
#     print('Скоро все наладится, не переживай')
# elif '?' in answer or 'не' in answer:
#     print('Извините, я вас не понимаю, ответьте точнее')
# else:
#     print('Извините, я вас не понимаю, ответьте точнее')


# 2.4
# print('Введите первое слово')
# word1 = input()
# print('Введите второе слово')
# word2 = input()
# if ('да' in word1 and 'нет' in word2) or ('да' in word2 and 'нет' in word1):
#     print('ВЕРНО')
# elif ('да' in word1 and 'да' in word2) or ('нет' in word1 and 'нет' in word2):
#     print('ВЕРНО')
# else:
#     print('НЕВЕРНО')


# 2.5
# print('Ответьте на несколько вопросов и получите строго индивидуальный анализ личностных качеств')
# print('Какое ваше любимое время года?')
# answer1 = input()
# while True:
#     if answer1 == 'зима' or answer1 == 'весна' or answer1 == 'осень' or answer1 == 'лето':
#         print('Какой цвет тебе нравится больше: красный, синий, желтый, зеленый?')
#         answer2 = input()
#     else:
#         print('Данные введены неверно. ОШИБКА')
#         break
#     if answer2 == 'красный' or answer2 == 'синий' or answer2 == 'желтый' or answer2 == 'зеленый':
#         print('Какое твое любимое животное: пингвин, лиса, енот?')
#         answer3 = input()
#     else:
#         print('Данные введены неверно. ОШИБКА')
#         break
#     if answer3 == 'пингвин' or answer3 == 'лиса' or answer3 == 'енот':
#         print('Сейчас вы получите результат теста')
#     else:
#         print('Данные введены неверно. ОШИБКА')
#         break
#     if answer1 == 'зима' and answer2 == 'синий' and answer3 == 'пингвин':
#         print('Вы самый крутой человек на свете')
#     elif answer1 == 'лето' and answer2 == 'желтый' and answer3 == 'лиса':
#         print('Вы очень солнечный человек')
#     elif answer1 == 'осень' and answer2 == 'красный' and answer3 == 'енот':
#         print('Вы хорошо разбираетесь в людях')
#     elif answer1 == 'весна' and answer2 == 'зеленый' and answer3 == 'лиса':
#         print('Вы умный человек')
#     elif answer1 == 'лето' and answer2 == 'желтый' and answer3 == 'енот':
#         print('Вы необыкновенный человек')
#     else:
#         print('Вы обычный человек без суперспособностей')
#     break
#

# 3.1
# print('Введите дробное число')
# number = float(input())
# if number > 0:
#     print('+')
# if number == 0:
#     print('0')
# if number < 0:
#     print('-')


# 3.2
# print('Введите два дробных числа и одну из математических операций(+, -, *, /)')
# number1 = float(input())
# number2 = float(input())
# line = input()
# if line == '+':
#     print(float(number1 + number2))
# elif line == '-':
#     print(float(number1 - number2))
# elif line == '*':
#     print(float(number1 * number2))
# elif line == '/' and number2 != 0:
#     print(float(number1 / number2))
# else:
#     print('888888')


# 3.3
# print('Введите год, чтобы определить високосный ли он')
# year = int(input())
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print('Високосный год')
# else:
#     print('Не високосный')


# 3.4
# print('Введите целое число')
# number = int(input())
# if number % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')


# 3.5
# print('Введите длинное имя')
# name = input()
# length = len(name) * 2 + 3
# print(length)


# 3.6
# print('Введите целое 3х-значное число')
# number = input()
# amount = len(set(number))
# if amount == 1:
#     print('В числе все цифры одинаковые')
# elif amount == 2:
#     print('В числе две одинаковые цифры')
# else:
#     print('OK')


# 3.7
# print('Введите трехзначное число')
# line = int(input())
# digit1 = int(line / 100)
# digit2 = int(line / 10 % 10)
# digit3 = int(line % 10)
# MAX = 0
# MIN = 1000
# if digit1 > digit2:
#     MAX = digit1
# else:
#     MAX = digit2
# if digit3 > MAX:
#     MAX = digit3
# if digit1 > digit2:
#     MIN = digit2
# else:
#     MIN = digit1
# if digit3 < MIN:
#     MIN = digit3
# if (MAX + MIN)/2 == digit1 or (MAX + MIN)/2 == digit2 or (MAX + MIN)/2 == digit3:
#     print('Вы ввели красивое число')
# else:
#     print('Жаль, вы ввели обычное число')


# 3.8
# print('Введите 3хзначное число')
# line = int(input())
# digit1 = int(line / 100)
# digit2 = int(line / 10 % 10)
# digit3 = int(line % 10)
# sum1 = digit1 + digit2
# sum2 = digit2 + digit3
# if sum1 > sum2:
#     print(str(sum1) + str(sum2))
# else:
#     print(str(sum2) + str(sum1))


# 3.9
# print('Введите любую строку для подсчета стоимости отправки сообщения')
# line = input()
# cost = len(line) * 40
# print(cost // 100, 'руб.', cost % 100, 'коп.')


# 4.1
# k = 1
# print('Введите любые фразы, а завершите разговор словом: Спасибо.')
# line = input()
# while line not in 'Спасибо.':
#     line = input()
#     k += 1
# print(k)


# 4.2
# k = 0
# amount = 0
# print('Введите температуру воздуха за несколько дней, чтобы обозначить конец ввода введите значение <-301')
# tem = float(input())
# while tem >= -300:
#     amount += tem
#     k += 1
#     tem = float(input())
# print('Средняя температура =', amount / k)


# 4.3
# import math
# print('Введите одно целое число для определения, является ли оно степенью двойки')
# number = int(input())
# if math.log(number, 2).is_integer():
#     print(int(math.log(number, 2)))
# else:
#     print('НЕТ')
#

# 4.4
# print('Введите пароль')
# password = input()
# print('Введите пароль еще раз')
# password1 = input()
# while True:
#     if len(password) < 8:
#         print('Короткий')
#         break
#     elif len(password) >= 8 and '123' in password:
#         print('Простой')
#     elif len(password) >= 8 and '123' not in password and password != password1:
#         print('Различаются')
#     else:
#         print('OK')
#     break


# 4.5
# print('Введите натуральное число')
# number = int(input())
# k = 0
# while number != 1:
#     if number % 2 == 0:
#         number = number//2
#         k += 1
#     else:
#         number = 3 * number + 1
#         k += 1
# print(k)

# 4.6
# print('Если введете числа, делящиеся на 10, программа будет продолжать работу')
# print('Если введете числа,  не делящиеся на 10, программа завершит работу')
# number = int(input())
# while number % 10 == 0:
#     number = int(input())


# 4.7 !!!
# print('Введите 2 числа: координаты клада по оси Х и по оси Y')
# X = int(input())
# Y = int(input())
# step = input()
# k = 0
# while step != 'стоп':
#     aim = int(input())
#     k += 1
#     if step == 'вперед':
#         k += 1
#     elif step == 'налево' or step == 'направо':
#         step = 'вперед'
#         k += 1
#     else:
#         step = 'вперед'
#         k += 1
# print(k)

# 4.8
# begin = 1
# end = 1000
# win = ''
# print('Загадай число от 1 до 1000, но не вводи его')
# while win != '=':
#     middle = (end + begin)//2
#     print(middle)
#     print('Введите <, > или =')
#     win = input()
#     if win == '>':
#         begin = middle
#     elif win == '<':
#         end = middle
#     elif win == '=':
#         print('Угадал')


# 5.1
# day = int(input('Введите день рождения '))
# month = int(input('Введите месяц рождения '))
# years = int(input('Введите год рождения '))
# century = years // 100
# year = years % 100
# if month < 3:
#     month += 10
# else:
#     month -= 2
# print((day + ((13 * month - 1) // 5) + year + (year // 4 + century // 4 - 2 * century + 777)) % 7)

# 5.2
# print('Введите необходимое колво камней в куче')
# n = int(input())
# steps = 0
# while n != 1:
#     if n % 2 == 0:
#         n /= 2
#     else:
#         n -= 1
#     steps += 1
# print('Необходимое колво шагов')
# print(steps)


# 5.3
# print('Введите начальное колво камней в 1 куче')
# n1 = int(input())
# print('Введите начальное колво камней во 2 куче')
# n2 = int(input())
# while n1 != 0 or n2 != 0:
#     print('Введите номер кучи, откуда берутся камни')
#     bunch = int(input())
#     print('Введите количество забираемых камней')
#     stones = int(input())
#     if bunch == 1:
#         if n1 - stones >= 0:
#             n1 -= stones
#     elif n2 - stones >= 0:
#         n2 -= stones
#     print('Оставшиеся камни в 1 куче', n1)
#     print('Оставшиеся камни во 2 куче', n2)


# 5.4
# print('Введите необходимое колво камней в куче')
# kol = int(input())
# while True:
#     if kol == 1 or kol == 2 or kol == 3 or kol == 5 or kol == 6 or kol == 7:
#         if kol == 2:
#             kol -= 2
#             print('Взято камней ИИ', 2, 'осталось камней', kol)
#         elif kol == 1:
#             kol -= 1
#             print('Взято камней ИИ', 1, 'осталось камней', kol)
#         elif kol == 3:
#             kol -= 3
#             print('Взято камней ИИ', 3, 'осталось камней', kol)
#         elif kol == 5:
#             kol -= 1
#             print('Взято камней ИИ', 1, 'осталось камней', kol)
#         elif kol == 6:
#             kol -= 2
#             print('Взято камней ИИ', 2, 'осталось камней', kol)
#         elif kol == 7:
#             kol -= 3
#             print('Взято камней ИИ', 3, 'осталось камней', kol)
#     else:
#         if kol % 2 == 0:
#             kol -= 1
#             print('Взято камней ИИ', 1, 'осталось камней', kol)
#         else:
#             kol -= 2
#             print('Взято камней ИИ', 2, 'осталось камней', kol)
#     if kol == 0:
#         print('ПРОИГРЫШ')
#         break
#     print('Введите сколько камней берете(от 1 до 3)')
#     n = int(input())
#     kol -= n
#     print('Взято камней', n, 'осталось камней', kol)
#     if kol == 0:
#         print('ВЫИГРЫШ')
#         break


# 5.5 АЙ НИД ХЭЛП
# print('Введите необходимое колво камней в куче')
# kol = int(input())
# while True:
#     if kol == 1 or kol == 2 or kol == 3 or kol == 5 or kol == 6 or kol == 7:
#         if kol == 2:
#             kol -= 1
#             print('Взято камней ИИ', 2, 'осталось камней', kol)
#         elif kol == 1:
#             kol -= 1
#             print('Взято камней ИИ', 1, 'осталось камней', kol)
#         elif kol == 3:
#             kol -= 2
#             print('Взято камней ИИ', 3, 'осталось камней', kol)
#         elif kol == 5:
#             kol -= 2
#             print('Взято камней ИИ', 1, 'осталось камней', kol)
#         elif kol == 6:
#             kol -= 3
#             print('Взято камней ИИ', 2, 'осталось камней', kol)
#         elif kol == 7:
#             kol -= 1
#             print('Взято камней ИИ', 3, 'осталось камней', kol)
#     else:
#         if kol % 2 == 0:
#             kol -= 1
#             print('Взято камней ИИ', 1, 'осталось камней', kol)
#         else:
#             kol -= 2
#             print('Взято камней ИИ', 2, 'осталось камней', kol)
#     if kol == 0:
#         print('ВЫИГРЫШ')
#         break
#     print('Введите сколько камней берете(от 1 до 3)')
#     n = int(input())
#     kol -= n
#     print('Взято камней', n, 'осталось камней', kol)
#     if kol == 0:
#         print('ПРОИГРЫШ')
#         break

# 5.6
# print('Введите начальное колво камней в 1 куче')
# n1 = int(input())
# print('Введите начальное колво камней во 2 куче')
# n2 = int(input())
# print('Введите начальное колво камней в 3 куче')
# n3 = int(input())
# while n1 != 0 or n2 != 0 or n3 != 0:
#     print('Введите номер кучи, откуда берутся камни')
#     bunch = int(input())
#     print('Введите количество забираемых камней')
#     stones = int(input())
#     if bunch == 1:
#         if n1 - stones >= 0:
#             n1 -= stones
#     if bunch == 2:
#         if n2 - stones >= 0:
#             n2 -= stones
#     if bunch == 3:
#         if n3 - stones >= 0:
#             n3 -= stones
#     print('Оставшиеся камни в 1 куче', n1)
#     print('Оставшиеся камни во 2 куче', n2)
#     print('Оставшиеся камни в 3 куче', n3)


# 5.7


# 5.8


# 6.1
# print('Введите колво секунд, оставшихся до запуска')
# n = int(input())
# for i in range(n, -1, -1):
#     print('Осталось секунд', i)
# print('Пуск')


# 6.2
# print('Введите высоту пирамиды')
# n = int(input())
# for i in range(n):
#     print(' ' * (n-i-1), '*' * (i*2+1))


# 6.3
# for i in range(0, 17):
#     print('Введите натуральное число')
#     d = int(input())
#     if i % d == 0:
#         print('ДА')
#     else:
#         print('НЕТ')


# 6.4
# Sum = 0
# print('Введите колво тестируемых людей')
# n = int(input())
# print('Введите на каждой новой строке IQ людей')
# i = 1
# while i <= n:
#     IQ = int(input())
#     Sum += IQ
#     avg = Sum / i
#     if IQ > avg:
#         print('>')
#     elif IQ < avg:
#         print('<')
#     else:
#         print('0')
#     i += 1


# 6.5 !!
# print('Введите колво дробинок')
# n = int(input())
# SumN = 0
# SumD = 1
# for i in range(n):
#     numerator = int(input())
#     denominator = int(input())
#     SumN = SumN * denominator + numerator * SumD
#     SumD *= denominator
# print(SumN, SumD)
# a = SumN
# b = SumD
# while a != 0 and b != 0:
#     if a > b:
#
#         a %= b
#     else:
#         b %= a
# gcd = a + b
# print(gcd)
# print(SumN // gcd, '/', SumD // gcd)


# 6.6
# import math
# print('Введите количество натуральных чисел')
# n = int(input())
# Sum = 0
# for i in range(1, n+1):
#     Sum += i**-2
# print(math.pi**2/Sum)


# 6.7
# print('Введите количество чисел')
# n = int(input())
# Sum = 0
# for i in range(n):
#     print('Введите натуральное число')
#     number = int(input())
#     if i % 2 == 0:
#         Sum += number
#     else:
#         Sum -= number
# print(Sum)


# 7.1
# print('Введите количество строк')
# n = int(input())
# cat = False
# print('Введите строки')
# for i in range(n):
#     line = input()
#     if 'Кот' in line or 'кот' in line:
#         cat = True
# if cat:
#     print('МЯУ')
# else:
#     print('НЕТ')


# 7.2
# print('Введите строки')
# cat = False
# line = input()
# i = 1
# k = 0
# while line != 'стоп':
#     if ('Кот' in line or 'кот' in line) and k == 0:
#         cat = True
#         k += 1
#         temp = i
#     i += 1
#     line = input()
# if cat:
#     print(temp)
# else:
#     print(-1)


# 7.3
# print('Введите колво строк')
# n = int(input())
# print('Введите строки')
# cat = False
# for i in range(n):
#     line = input()
#     if 'Кот' in line or 'кот' in line:
#         cat = True
#         break
# if cat:
#     print('МЯУ')
# else:
#     print('НЕТ')


# 7.4
# print('Введите строки')
# cat = False
# line = input()
# i = 1
# k = 0
# while line != 'стоп':
#     if 'Кот' in line or 'кот' in line:
#         cat = True
#         k = i
#         break
#     else:
#         cat = False
#     i += 1
#     line = input()
# if cat:
#     print(k)
# else:
#     print(-1)


# 7.5
# print('Введите строки')
# line = input()
# k = 0
# cat = -1
# i = 1
# while line != 'стоп':
#     if ('Кот' in line or 'кот' in line) and k == 0:
#         cat = i
#     if 'Кот' in line or 'кот' in line:
#         k += 1
#     i += 1
#     line = input()
# print('Общее количество строк с котом:', k)
# print('Номер строки, где впервые был кот или -1, если кота нет:', cat)


# 7.6 !!!
# print('Введите 2 числа: координаты клада по оси Х и по оси Y')
# X0 = int(input())
# Y0 = int(input())
# X = 0
# Y = 0
# print('Введите указания: север, юг, запад или восток или стоп')
# step = input()
# while step != 'стоп':
#     if step == 'север':
#         print('Введите колво шагов, которые необходимо пройти')
#         aim = int(input())
#         Y += aim
#     elif step == 'юг':
#         print('Введите колво шагов, которые необходимо пройти')
#         aim = int(input())
#         Y -= aim
#     elif step == 'запад':
#         print('Введите колво шагов, которые необходимо пройти')
#         aim = int(input())
#         X -= aim
#     elif step == 'восток':
#         print('Введите колво шагов, которые необходимо пройти')
#         aim = int(input())
#         X += aim
#     print('Введите указания: север, юг, запад или восток или стоп')
#     step = input()
# if X == X0 or Y == Y0:
#     print(2)
# else:
#     print(3)


# 7.7
# print('Введите колво строк')
# n = int(input())
# print('Введите строки')
# cat = False
# for i in range(n):
#     line = input()
#     if 'Кот' in line or 'кот' in line:
#         cat = True
#         if 'Пёс' in line or 'пёс' in line:
#             cat = False
#     if 'Пёс' in line or 'пёс' in line:
#         cat = False
#         if 'Кот' in line or 'кот' in line:
#             cat = True
# if cat:
#     print('МЯУ')
# else:
#     print('НЕТ')


# 7.8
# print('Введите число - запас терпения учителя')
# n = int(input())
# print('Вводите отсчет: раз, два, три, четыре')
# right = 0
# mistake = 0
# while True:
#     line1 = input()
#     if line1 == 'раз':
#         right += 1
#         line2 = input()
#         if line2 == 'два':
#             right += 1
#             line3 = input()
#             if line3 == 'три':
#                 right += 1
#                 line4 = input()
#                 if line4 == 'четыре':
#                     right += 1
#                 else:
#                     print('Правильных отсчетов было', right, 'но теперь вы ошиблись.')
#                     mistake += 1
#                     right = 0
#             else:
#                 print('Правильных отсчетов было', right, 'но теперь вы ошиблись.')
#                 mistake += 1
#                 right = 0
#         else:
#             print('Правильных отсчетов было', right, 'но теперь вы ошиблись.')
#             mistake += 1
#             right = 0
#     else:
#         print('Правильных отсчетов было', right, 'но теперь вы ошиблись.')
#         mistake += 1
#         right = 0
#     if mistake == n:
#         print('На сегодня хватит.')
#         break
#     if n == 0 and mistake == 1:
#         print('На сегодня хватит.')
#         break


# 7.9
# line = ''
# while line != 'x':
#     print('Введите первое число')
#     n1 = int(input())
#     print('Введите операцию: +, -, *, /, %, ! или x для завершения')
#     line = input()
#     if line == 'x':
#         print(n1)
#         break
#     else:
#         if line == '+':
#             print('Введите второе число')
#             n2 = int(input())
#             print(n1 + n2)
#         elif line == '-':
#             print('Введите второе число')
#             n2 = int(input())
#             print(n1 - n2)
#         elif line == '*':
#             print('Введите второе число')
#             n2 = int(input())
#             print(n1 * n2)
#         elif line == '/':
#             print('Введите второе число')
#             n2 = int(input())
#             if n2 == 0:
#                 continue
#             else:
#                 print(n1 // n2)
#         elif line == '%':
#             print('Введите второе число')
#             n2 = int(input())
#             print(n1 % n2)
#         elif line == '!' and n1 > 0:
#             k = 1
#             for i in range(1, n1+1):
#                 k *= i
#             print(k)
#         elif line == '!' and n1 == 0:
#             print(1)


# 7.10
# price = 1
# last_price = 0
# increase = False
# decrease = False
# price_buy = 0
# price_sale = 0
# k = 0
# while price != 0:
#     last_price = price
#     print('Введите цену акций в некоторое количество дней')
#     price = int(input())
#     k += 1
#     if last_price < price and not increase and k > 1 and not decrease:
#         price_buy = price
#         increase = True
#     elif last_price > price and increase and not decrease:
#         price_sale = price
#         decrease = True
# print(price_buy, price_sale, (price_sale - price_buy))


# 8.1
# print('Введите число колонок в таблице')
# column = int(input())
# print('Введите число строк в таблице')
# row = int(input())
# for i in range(1, row + 1):
#     for j in range(1, column + 1):
#         print(j / i, end='\t')
#     print()

# 8.2
# print('Введите высоту прямоугольника')
# height = int(input())
# print('Введите ширину прямоугольника')
# width = int(input())
# print('Введите символ для рисования прямоугольника')
# symbol = input()
# for i in range(height):
#     if i == 0 or i == height - 1:
#         for j in range(width):
#             print(symbol, end='')
#     else:
#         print(symbol, end='')
#         for j in range(1, width - 1):
#             print(' ', end='')
#         print(symbol, end='')
#     print()


# 8.3
# print('Введите размер выделяемой субсидии')
# price = int(input())
# print('Введите колво голов скота, которые надо купить')
# kol = int(input())
# for b in range(1, price // 20 + 1):
#     for k in range((price - b * 20) // 10 + 1):
#         t = kol - b - k
#         if b * 20 + k * 10 + t * 5 == price:
#             print(b, k, t)


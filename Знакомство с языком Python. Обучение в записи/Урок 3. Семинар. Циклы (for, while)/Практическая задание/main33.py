#                                                               Задача 3. Игра «Угадай число»

# Папа-программист написал для сына программу, которая просит его угадать число. Недостаток программы был в том, что бедному сыну приходилось её каждый раз перезапускать, чтобы
# угадывать число. Теперь, когда мы знаем гораздо больше, пришло время исправить этот недостаток и заодно немного улучшить саму игру.

# Напишите программу-игру, которая запрашивает у пользователя число до тех пор, пока он его не отгадает. Выводите сообщения в соответствии с примером.

# Пример (загадали число 7)

# Введите число: 3
# Число меньше, чем нужно. Попробуйте ещё раз!
# Введите число: 10
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 8
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 7
# Вы угадали! Число попыток: 4
 
#                                                            Подсказка № 1

# Используйте бесконечный цикл while True, чтобы повторно запрашивать ввод числа у пользователя до тех пор, пока он не угадает загаданное число. Цикл должен завершаться только
# при правильном ответе.

#                                                           Подсказка № 2

# Создайте переменную для хранения загаданного числа. Это число нужно угадать. Также создайте переменную для подсчета количества попыток угадывания (guess_count) и увеличивайте
# её при каждой новой попытке.

#                                                           Подсказка № 3

# Для ввода числа от пользователя используйте функцию input(), а затем преобразуйте введенное значение в целое число с помощью int(). Это число нужно сравнивать с загаданным
# числом.

#                                                           Подсказка № 4

# Используйте условные конструкции (if, elif, else) внутри цикла для проверки введенного числа. Если оно больше загаданного, выведите сообщение, что число слишком велико. Если
# оно меньше, выведите сообщение, что число слишком мало. Если угадали, выведите сообщение об успехе и количество попыток, после чего завершите цикл с помощью break.

#                                                           Эталонное решение:

number = 7 # Загаданное число, которое нужно угадать
guess_count = 0 # Счетчик количества попыток

while True: # Бесконечный цикл для повторного запроса числа у пользователя
    guess_num = int(input('Введите число: ')) # Ввод числа пользователем
    guess_count += 1 # Увеличиваем счетчик попыток

# Проверка, больше ли введенное число, чем загаданное
    if guess_num > number:
        print('Число больше, чем нужно. Попробуйте ещё раз!')

# Проверка, меньше ли введенное число, чем загаданное
    elif guess_num < number:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')

# Если число угадано правильно
    else:
        print('Вы угадали! Число попыток:', guess_count)
        break # Прерываем цикл, так как число угадано






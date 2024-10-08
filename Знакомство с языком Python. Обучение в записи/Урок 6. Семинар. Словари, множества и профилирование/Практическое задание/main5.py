#                                                               Задача 5. Словарь синонимов

# Одна библиотека поручила вам написать программу для оцифровки словарей синонимов. На вход в программу подаётся N пар слов. Каждое слово является синонимом для своего парного слова.
# Реализуйте код, который составляет словарь синонимов (все слова в словаре различны), затем запрашивает у пользователя слово и выводит на экран его синоним. Обеспечьте контроль
# ввода: если такого слова нет, выведите ошибку и запросите слово ещё раз. При этом проверка не должна зависеть от регистра символов

#                                                                           Пример

# Введите количество пар слов: 3
# Первая пара: Привет — Здравствуйте
# Вторая пара: Печально — Грустно
# Третья пара: Весело — Радостно
# Введите слово: интересно
# Такого слова в словаре нет.
# Введите слово: здравствуйте
# Синоним: Привет

#                                                                           Подсказка № 1

# Перед созданием словаря синонимов, убедитесь, что вы корректно принимаете пары слов. Разделите входные данные по символу « - » и приведи слова к нижнему регистру для унификации
# ввода. Это позволит избежать ошибок, связанных с разным регистром символов.

#                                                                           Подсказка № 2

# Для добавления слов в словарь, каждую пару слов следует добавить как ключ и значение в словарь. Не забудьте добавить оба направления синонимов (например, если «Привет» является
# синонимом для «Здравствуйте», то «Здравствуйте» также должно быть синонимом для «Привет»).

#                                                                           Подсказка № 3

# После создания словаря синонимов, запускайте бесконечный цикл для ввода слова от пользователя. Убедитесь, что слово, введенное пользователем, также приводится к нижнему регистру
# для проверки.

#                                                                           Эталонное решение:

# Создаем пустой словарь для хранения синонимов
synonyms_dict = dict()
# Запрашиваем количество пар слов у пользователя
pairs_count = int(input('Введите количество пар слов: '))
# Проходим по каждой паре слов
for i_pair in range(pairs_count):
# Запрашиваем пару слов, разделенных " - "
# Приводим слова к нижнему регистру для корректной работы с различными регистрами
    first_word, second_word = input(f'{i_pair + 1} пара:').lower().split(' - ')
# Добавляем пары в словарь
synonyms_dict[first_word] = second_word
synonyms_dict[second_word] = first_word
# Запускаем бесконечный цикл для ввода слова и поиска синонима
while True:
# Запрашиваем слово у пользователя и приводим его к нижнему регистру
    word = input('Введите слово: ').lower()
# Проверяем, есть ли слово в словаре
    if word in synonyms_dict:
# Если есть, выводим синоним, приводя его к начальной букве заглавной
        print('Синоним: ', synonyms_dict[word].capitalize())
        break
    else:
# Если нет, выводим сообщение об ошибке
        print('Такого слова в словаре нет.')
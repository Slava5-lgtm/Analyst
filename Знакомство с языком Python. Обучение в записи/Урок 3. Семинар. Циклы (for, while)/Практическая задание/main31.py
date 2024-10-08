#                                                      Задание 1: Поставьте оценку!

# Вася выложил своё новое приложение на платформу для начинающих разработчиков, на ней пользователи могут ставить оценку приложению: от −100 до 100. Ему захотелось сравнить
# количество положительных и отрицательных отзывов, для этого он заранее отфильтровал все отзывы так, чтобы в конце были те, которые равны нулю. 

# Напишите программу, которая находит количество положительных и количество отрицательных чисел в последовательности. Последовательность заканчивается на числе 0.

#                                                        Пример
# Введите число: −4
# Введите число: −90
# Введите число: 6
# Введите число: 0
# Кол-во положительных чисел: 1
# Кол-во отрицательных чисел: 2

#                                                        Подсказка № 1

# Для решения задачи используйте цикл while. Он должен работать до тех пор, пока вводимое число не будет равно 0. Это число будет служить сигналом к завершению ввода и
# завершению программы.

#                                                       Подсказка № 2
# Инициализируйте две переменные для подсчета положительных и отрицательных чисел. Начальные значения этих переменных должны быть равны нулю.

#                                                       Подсказка № 3

# Внутри цикла while проверяйте введенное число. Если число больше нуля, увеличьте счетчик положительных чисел. Если меньше нуля — увеличьте счетчик отрицательных чисел. Число
# 0 не учитывается ни в одном из счетчиков.

#                                                       Подсказка № 4

# Не забудьте обновлять переменную rating внутри цикла. Это нужно для того, чтобы пользователь мог вводить новые значения чисел на каждой итерации цикла.

#                                                       Эталонное решение:

# Ввод первого числа
rating = int(input('Введите число: '))
# Инициализация счетчиков положительных и отрицательных чисел
positive_count = 0
negative_count = 0
# Цикл продолжается до тех пор, пока не введено число 0
while rating != 0:
# Увеличиваем счетчик положительных чисел, если число больше 0
    if rating > 0:
        positive_count += 1
# Увеличиваем счетчик отрицательных чисел, если число меньше 0
    else:
        negative_count += 1
# Ввод следующего числа
    rating = int(input('Введите число: '))
# Вывод количества положительных и отрицательных чисел
print('Кол-во положительных чисел:', positive_count)
print('Кол-во отрицательных чисел:', negative_count)  
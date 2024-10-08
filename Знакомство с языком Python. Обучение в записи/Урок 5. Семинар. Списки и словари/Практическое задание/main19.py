#                                                           Задание 1. 
#                                                                       Видеокарты

# В базе магазина электроники есть список видеокарт компании NVIDIA разных поколений. Вместо полных названий хранятся только числа, которые обозначают модель и поколение
# видеокарты. Недавно компания выпустила новую линейку видеокарт. Самые старшие поколения разобрали за пару дней.

# Напишите программу, которая удаляет наибольшие элементы из списка видеокарт.

#                                                                       Пример:

# Количество видеокарт: 5
# Видеокарта 1: 3070
# Видеокарта 2: 2060
# Видеокарта 3: 3090
# Видеокарта 4: 3070
# Видеокарта 5: 3090
# Старый список видеокарт: [ 3070 2060 3090 3070 3090 ]
# Новый список видеокарт: [ 3070 2060 3070 ]

#                                                                       Подсказка № 1

# Для начала получите количество видеокарт от пользователя и создайте пустые списки для хранения введённых видеокарт и нового списка без наибольших элементов.

#                                                                       Подсказка № 2

# Используйте цикл для ввода номеров видеокарт. Во время ввода также определите наибольшую видеокарту, обновляя переменную maxItem при каждом вводе, если текущий элемент
# больше предыдущего максимума.

#                                                                       Подсказка № 3

# После ввода всех видеокарт, пройдитесь по списку и создайте новый список, в который добавляйте только те видеокарты, которые не равны максимальному значению, найденному
# ранее.

#                                                                       Подсказка № 4

# Для вывода старого списка видеокарт, используйте цикл, чтобы пройти по всем элементам списка и распечатать их в требуемом формате. Для вывода нового списка видеокарт,
# сделайте то же самое, что и для старого списка, но с новым списком, который не содержит наибольших значений. Убедитесь, что формат вывода совпадает с требуемым.

#                                                                       Эталонное решение:

# Ввод количества видеокарт
videoСardsNumber = int(input('Введите количество видеокарт: '))

# Инициализация списка для хранения видеокарт
videoСards = []
newVideoCardsList = []
maxItem = 0

# Заполнение списка видеокарт и определение наибольшего элемента
for item in range(videoСardsNumber):

    # Ввод номера видеокарты и добавление в список
    videoСards.append(int(input(f'Видеокарта {item + 1}: ')))

# Обновление значения максимального элемента
if videoСards[item] > maxItem:
    maxItem = videoСards[item]

# Формирование нового списка без наибольших элементов
for item in range(videoСardsNumber):
    if videoСards[item] != maxItem:
        newVideoCardsList.append(videoСards[item])

# Вывод старого списка видеокарт
print()
print('Старый список видеокарт: [', end=' ')
for item in range(videoСardsNumber):
    print(videoСards[item], end=' ')
print(']')

# Вывод нового списка видеокарт
print('Новый список видеокарт: [', end=' ')
for item in range(len(newVideoCardsList)):
    print(newVideoCardsList[item], end=' ')
print(']')

#                                                       Задача №2.

# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. Определите, сколько
# различных слов содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore
# shells
# Output: 13 (В отом предложении 13 различных слов)

stroka = input(" Введите текст ").split() # Вводим строку и приобразовываем в масив при помощи функции .split()

# У нас идет речь о уникальности (различные слова). Усли мы говорим о уникальности значит нам нужно использовать множемтво
set_1 = set() # Создадим его

for i in stroka: # Теерь пройдемся по всему масиву
    set_1.add(i.lower()) # И при каждой итерации будем наше множество set_1 добовлять (add) нашу переменую i но так как у нас идет речь о различных словах то есть уникальности у нас
                       # они могут быть написаны как с большой буквы так и с маленькой. Будем преобразовывать их в маленький регистр при помощи функции lower
print(len(set_1))   # И далее выводим сколько слов у нас есть, мы будем считать его размер 
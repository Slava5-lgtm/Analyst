#                                                       Задача №1.

# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса
# формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2 (Буква а уже встречелась один раз поэтому сдесь (a a) мы должны вывести (a_1) сдесь буква (а) встречалось два раза выводим (a a_1 a_2)
# и.т.д.)
# Для решения данной задачи используйте функцию .split()

# stroka = input(" Ведите символы ")  # создадим переменую stroka и будем использовать функцию input() для ввода
# print(stroka) # Выводим нашу строку здесь
# Мы видем что сначало была строка j u i o
# stroka = stroka.split() # Далее будем ее преобразовывать нашу переменую stroka в масив с помощю функции split
# stroka = stroka.split(',')
# print(stroka) # и выводим после преоброзования 
# Далее после функции split наша строка преоброзовалась в масив ['j', 'u', 'i', 'o'] в скобках split( можго вставит совершено любое значения оно будит считаться как разделитель)

stroka = input(" Ведите символы ").split()  # Можно преобразовывать фунцию split сразу после ввода 
res = {} # Создаем словарь в котором хрониться наше значение будет называться res и он будет пустой {}

for i in stroka: # Создаем цикл в котором проходить будем по всему нашему масиву
    if i in res: # Делаем проверку если (if) наша переменая то есть наша буква (i) есть в нашем результате res
       print(f'{i}_{res[i]}', end=' ') # То мы будем выводить так как на сказана в примере наша буква _ и сколько раз она уже встречалось
    else: # Если else
        print(i, end=' ') # нашей буквы нет в нашем словаре мы выводим    
    # При каждой итерации нашего цикла мы будем в наш словарь res добовлять новое значение либо если этого значения уже есть добовлять к ключю еденицу

    res[i] = res.get(i , 0) +1 # Мы оброщяемся к словорю res и к лючю [i] далее = res используем функцию .get(i , 0) (в этуфункцию мы передаем два значения ключ (i) второе это
                            # декфолтное значения (это обозначает мы оброшяемся к словорю по ключу (i) мы хотим полдучит значения если его нету у нас возврощяеться (0))) и + 1 если
                            # на вход поступает какая то новое буква мы в нашем словаре res это новое значения  
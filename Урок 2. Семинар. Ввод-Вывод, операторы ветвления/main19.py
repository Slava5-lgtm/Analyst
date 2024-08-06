# Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»; это зависит от того, в
# какую сторону едет электричка). В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозожно.

#                   Input: 3 4(ввод на разных строках)
#                   Output: 6

# Первым действием нам нужно ввести два числа будем это делать при помоши кострукции int(input())

print('В какой по счету вагон сел Витя?')
i = int(input())
print('Какой номер вагона у Вити?')
j = int(input())

# Первым дествием давайти свами определим когда мы не сможем решить нашу задачу. Тоесть когда мы не сможем сказать сколько вагонов содержиться в нашей электричке. Это
# будет толко тогда когда наша переменая (i) будет равняться переменой (j). Это будет озночать что нумерация вагонов начинаеться с начало поезда соотвествено наши переменые
# (i) равняться переменой (j) и сколько вагонов после насмы не будем знать. Так как мы знаем только число с начало.
 
#                                                           Соотвествено надо сделать проверку

if i - j == 0:     # если разность нашех чисел i - j равняеться нулю то мы не сможем дать наш верный результат
    print(-1)      # И будем выводить -1
else:              # а иначе
    print(f'В нашей элекрички - {i+j-1} вагонов')   # если нумерация начинаеится с конца поезда то мы будем уже выдовать верный результат соотвествено давайте будим складывать два числа i и j чтобы знать сколько вагонов у нас всего но мы также будим вычитать единицу так как наш вагон будит считаться два раза 
    
#                                   Проверяем

# В какой по счету вагон сел Витя?
# 3
# Какой номер вагона у Вити?
# 4
# В нашей элекрички - 6 вагонов

# Тоесть мы сидим в третем вагоне с начало поезда и в четвертом с конца. Всего у нас шесть вагонов
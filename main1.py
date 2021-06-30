# Задание № 1:
# Выяснить тип результата выражений:

multiply = 15 * 3
print(multiply, (type(multiply)))
division = 15 / 3
print(division, (type(division)))
whole_division = 15 // 2
print(whole_division, (type(whole_division)))
cube = 15 ** 2
print(cube, (type(cube)))




# Задание № 2:

# Дан список:

# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!



data_list = []
some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
data_list1 = ''

for elem in some_list:
    if elem.isdigit():
        if len(elem) == 1:
            elem = f'0{elem}'
        data_list.append('"')
        data_list.append(elem)
        data_list.append('"')
    elif elem[1:].isdigit():
        if len(elem[1:]) == 1:
            elem = f'{elem[:1]}0{elem[1:]}'
        data_list.append('"')
        data_list.append(elem)
        data_list.append('"')
    else:
        data_list.append(elem)

space = False
for i, elem in enumerate(data_list):
    prefix = ' '
    if i == 0 or space:
        prefix = ''
    data_list1 += f'{prefix}{elem}'
    if elem == '"':
        space = not space
print(data_list1)






# Задание № 3:

# Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
#
# Известно, что имя сотрудника всегда в конце строки. Сформировать из этих имён и вывести на экран фразы вида: 'Привет, Игорь!'
# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. Можно ли при этом не создавать новый список?


employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in range(len(employees)):
    employees[i] = employees[i].split()
    name = employees[i].pop()
    print(f'Привет, {name.capitalize()}!')





# Задание № 4:
# Создать вручную список, содержащий цены на товары (10–20 товаров)

def prices(elements):
    elements_rub = []
    for i in range(len(elements)):
        rub = int(elements[i] // 1)
        cop = int((elements[i] * 100) % 100)
        if cop == 0:
            cop = '00'
        elements_rub.append(f'{rub} руб {cop} коп')

    return elements_rub

price = [38.72, 41.84, 25.55, 38, 98.98, 24.41, 53.68]


# A.

print(prices(price))

# B.

print(prices(price), id(price))
price.sort()
print(prices(price), id(price))

#С.

my_price = price.copy()
my_price.sort(reverse = True)
print(prices(my_price))

#D.
print(prices(price[-5:]))




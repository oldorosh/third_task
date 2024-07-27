separator = input('Введите разделитель, которым будуте пользоваться: ')

custom_list = list(map(int, input('Введите элементы списка с выбранным: ').split(separator)))
print(list(set(custom_list)))

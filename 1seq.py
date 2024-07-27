amount = int(input('Введите количество элементов: '))

list_number = []
i = 0
while i < amount:
    num = int(input(f'Введите {i} элемент: '))
    list_number.append(num)
    i += 1

print(list_number)

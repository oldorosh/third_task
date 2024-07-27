first_list = list(map(int, input('Введите элементы первого списка через пробел: ').split()))
second_list = list(map(int, input('Введите элементы второго списка через пробел: ').split()))

while True:
    if len(set(first_list)&set(second_list)) != 0:
        intersection = list(set(first_list)&set(second_list))
        for num in intersection:
            first_list.remove(num)
    else:
        break

print(first_list)


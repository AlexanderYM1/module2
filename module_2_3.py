# Первый вариант решения.
'''my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while my_list[i] > 0:
    print (my_list[i])
    i = i + 1
    if my_list[i]==0:
        i = i + 1
        continue'''
# Второй вариант решения
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i <= len(my_list):
    n = my_list[i]
    if n < 0:
        break
    if n == 0:
        i = i + 1
        continue
    print(n)
    i = i + 1
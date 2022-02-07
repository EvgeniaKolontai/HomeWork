#По заданному номеру дня недели вывести его название

print('Введите число')
list = ['Mon', 'Tue', 'Wen' 'Thus', 'Fri', 'Sat', 'Sun']
a = int(input())
if a < 5:
    print(f'Будние -{list[a-1]}')
else :
    print(f'Выходные-{list[a-2]}')

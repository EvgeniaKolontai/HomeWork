#1.По двум заданным числам проверять является ли первое квадратом второго.
print('Введите а');
a = int(input())
print('Введите b');
b = int(input())
if (a == b * b):
    print('Первое число квадрат второго')
elif a != b * b :
    print('Первой чиcло не квадрат второго')
    
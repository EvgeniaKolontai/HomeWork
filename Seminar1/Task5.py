#5. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа.
print('Введите число : ')
a = int(input())
nums = list(range(10, 99))
print(nums[a-1]) 
b = nums[a-1] // 10
c = nums[a-1] % 10
if b > c :
    print(f'{b} найбольшая цифра из числа {nums[a-1]}')
if c > b :
     print(f'{c} найбольшая цифра из числа {nums[a-1]}')
if c == b :
    print(f'Цифры числа {nums[a-1]} равны ')


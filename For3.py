# Даны два целых числа A и B (A < B). Вывести в порядке убывания все целые числа, расположенные между A и B
# (не включая числа A и B), а также количество N этих чисел.

a = int(input())
b = int(input())
n = 0
for i in range(b - 1, a, -1):
    n += 1
    print(i)
print(n)

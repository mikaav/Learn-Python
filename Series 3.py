# Даны десять вещественных чисел. Найти их среднее арифметическое.
c = 1
b = 1
for i in range(10):
    a = float(input())
    b += a
    c = b / i
print(c)

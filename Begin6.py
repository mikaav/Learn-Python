# Даны длины ребер a, b, c прямоугольного параллелепипеда. Найти его объем V = a·b·c и площадь поверхности S = 2·(a·b + b·c + a·c)

a = int(input())
b = int(input())
c = int(input())
v = a * b * c
s = a * b + b * c + a * c
print("Obyom V = ", v)
print("Ploshad S = ", s)

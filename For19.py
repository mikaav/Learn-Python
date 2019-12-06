# Дано целое число N (> 0). Найти произведение N! = 1·2·...·N (N–факториал).

n = int(input())
f = 0
if n > 0:
    f = 1
for i in range(1, n + 1):
    f *= i
print(f)

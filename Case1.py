# Дано целое число в диапазоне 1–7. Вывести строку — название дня недели,
# соответствующее данному числу (1 — «понедельник», 2 — «вторник» и т. д.)

d = int(input())
if d == 1:
    print("Monday")
elif d == 2:
    print("Tuesday")
elif d == 3:
    print("Wednesday")
elif d == 4:
    print("Thursday")
elif d == 5:
    print("Friday")
elif d == 6:
    print("Saturday")
elif d == 7:
    print("Sunday")

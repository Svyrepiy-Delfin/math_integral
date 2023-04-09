import math
import matplotlib.pyplot as plt


def left_sum(n):
    dx = math.pi / n
    x = 0
    sum = 0
    for i in range(n):
        sum += math.sin(x)
        x += dx
    return dx * sum


def right_sum(n):
    dx = math.pi / n
    x = dx
    sum = 0
    for i in range(n):
        sum += math.sin(x)
        x += dx
    return dx * sum


def middle_sum(n):
    dx = math.pi / n
    x = dx / 2
    sum = 0
    for i in range(n):
        sum += math.sin(x)
        x += dx
    return dx * sum


n = int(input("Введите количество разбиений: "))
print("Выберите способ:")
print("1 - левые, 2 - правые, 3 - средние")
method = int(input())

if method == 1:
    sum = left_sum(n)
    title = "Интегральная сумма (левые): " + str(sum)
elif method == 2:
    sum = right_sum(n)
    title = "Интегральная сумма (правые): " + str(sum)
elif method == 3:
    sum = middle_sum(n)
    title = "Интегральная сумма (средние): " + str(sum)

x = []
y = []
dx = math.pi / n
for i in range(n + 1):
    x.append(i * dx)
    y.append(math.sin(i * dx))

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y=sin(x)")

if method == 1:
    for i in range(n):
        x = [i * dx, (i + 1) * dx, (i + 1) * dx, i * dx, i * dx]
        y = [0, 0, math.sin(i * dx), math.sin(i * dx), 0]
        plt.fill(x, y, alpha=0.3, color='r')
elif method == 2:
    for i in range(n):
        x = [i * dx, (i + 1) * dx, (i + 1) * dx, i * dx, i * dx]
        y = [0, 0, math.sin((i + 1) * dx), math.sin((i + 1) * dx), 0]
        plt.fill(x, y, alpha=0.3, color='b')
elif method == 3:
    for i in range(n):
        x = [i * dx, (i + 1) * dx, (i + 1) * dx, i * dx, i * dx]
        y = [0, 0, math.sin(i * dx + dx / 2), math.sin(i * dx + dx / 2), 0]
        plt.fill(x, y, alpha=0.3, color='g')

plt.title(title)
plt.show()


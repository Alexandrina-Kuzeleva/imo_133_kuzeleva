import random
import time
import heapq

def heapsort(x):
    heapq.heapify(x)
    sortedlist = []
    for i in range(len(x)-1, -1, -1):
        sortedlist.append(heapq.heappop(x))
    return sortedlist

def quicksort(x):
   if len(x) <= 1:
       return x
   else:
       q = random.choice(x)
   bh = [i for i in x if i < q]
   sl = [q] * x.count(q)
   af = [i for i in x if i > q]
   return quicksort(bh) + sl + quicksort(af)

def combsort(x):
    fac = 1.247
    stp = len(x) - 1
    while stp >= 1:
        for i in range(len(x) - int(stp)):
            if x[i] > x[i + int(stp)]:
                x[i], x[i + int(stp)] = x[i + int(stp)], x[i]
        stp /= fac
    for i in range(len(x) - 1):
        for j in range(len(x) - i - 1):
            if x[j + 1] < x[j]:
                x[j], x[j + 1] = x[j + 1], x[j]

    return x

array = [random.randint(0,999999) for i in range(1000)]

a1 = []
a2 = []
a3 = []
for i in range(1000):
    n = random.randint(0,999999)
    a1.append(n)
    a2.append(n)
    a3.append(n)

print(a1)
print('_____________________________________')
print('Пирамидальная сортировка')
t1 = time.time()
print(heapsort(a1))
t2 = time.time()
print(t2-t1)
print('_____________________________________')
print('Быстрая сортировка')
t1 = time.time()
print(quicksort(a2))
t2 = time.time()
print(t2-t1)
print('_____________________________________')
print('Сортировка расчёской')
t1 = time.time()
print(combsort(a3))
t2 = time.time()
print(t2-t1)
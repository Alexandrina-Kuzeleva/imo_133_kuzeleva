count = 0
n = int(input())
for i in range(1, n+1):
    if n%i==0:
        count += i
    else:
        continue
print(count)
flag =  0
for i in range(1,10+1):
    num = int(input())
    if num % 2 == 0:
        flag += 1
    else:
        continue
if flag == 10:
    print('YES')
else:
    print('NO')
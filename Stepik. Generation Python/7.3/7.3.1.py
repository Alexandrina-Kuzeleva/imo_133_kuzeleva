num1 = int(input())
num2 = int(input())
count = 0
for i in range(num1, num2+1):
    if (i**3)%10==4 or (i**3)%10==9:
        count += 1
    else:
        continue
print(count)

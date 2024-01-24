n = int(input())
mx1 = 0
mx2 = 0
for i in range(1,n+1):
    num = int(input())
    if mx2 < num < mx1:
        mx2 = num
    if num > mx1:
        mx2 = mx1
        mx1 = num
print(mx1)
print(mx2)

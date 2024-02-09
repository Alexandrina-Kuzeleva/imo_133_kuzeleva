a = int(input())
if a%2!=0:
    print('YES')
elif 2<=a<=5 and a%2==0:
    print('NO')
elif 6<=a<=20 and a%2==0:
    print('YES')
elif a%2==0 and a>20:
    print("NO")

a = int(input())
b = (a//1000)+(a%10)
c = ((a%1000)//100) - ((a%100)//10)
if b==c:
    print('ДА')
else:
    print('НЕТ')
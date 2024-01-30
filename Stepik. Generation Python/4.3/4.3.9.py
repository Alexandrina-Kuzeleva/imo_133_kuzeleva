a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a2 > b1 or a1 > b2:  
    print('пустое множество')
elif a1 == b2: 
    print(a1)
elif a2 == b1: 
    print(a2)
else:  
    if a1 > a2: 
        a2 = a1
    if b1 < b2: 
        b2 = b1
    print(a2, b2)

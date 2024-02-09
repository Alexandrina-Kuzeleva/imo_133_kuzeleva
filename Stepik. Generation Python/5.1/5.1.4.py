roman_n = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
n = int(input())
if 1 <= n <= 10:
    print(roman_n[n-1])
else:
    print('ошибка')
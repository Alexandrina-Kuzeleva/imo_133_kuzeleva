a = input()
b = input()
if a == b and ( a == 'красный' or a == 'синий' or a == 'желтый'):
    print(a)
elif (a == 'красный' and b == 'синий') or (a == 'синий' and b == 'красный'):
    print('фиолетовый')
elif (a == 'красный' and b == 'желтый') or (a == 'желтый' and b == 'красный'):
    print('оранжевый')
elif (a == 'желтый' and b == 'синий') or (a == 'синий' and b == 'желтый'):
    print('зеленый')
else:
    print("ошибка цвета")
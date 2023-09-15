from datetime import datetime

x = datetime(2005, 6, 24)
d = datetime(2023,9,1)
a = d-x
print(str(a)[:-14])

import math
G=6.6743*math.pow(10,-11)
def f(m2,R):
    m1=5.97600*math.pow(10,24)
    return (G*m1*m2)/math.pow(R,2)

R = 100000
print(f(int(str(a)[:-14])*math.pow(10,3),R*math.pow(10,3)))


'''
дз доп:
разница между 01.09.2023 и вашим ДР - масса в тоннах расстоянии 100000км
масса 6643т 6643000кг'''

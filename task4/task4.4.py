from collections import Counter

def spl(s):
    for i in s:
        if '\n' in i:
            a = i.split('\n')
            for j in a:
                s.append(j)
            s.remove(i)
    return s

crime = open('crime.txt').read().split(' ') #преступление и наказание
'''war = open('war.txt').read().split(' ')''' #война и мир надо опимизировать код
'''print(spl(crime))
print(Counter(crime))'''
print(Counter(spl(crime)))
'''print(Counter(spl(war)))'''
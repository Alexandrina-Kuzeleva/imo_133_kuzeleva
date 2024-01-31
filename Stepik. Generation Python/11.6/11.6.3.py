s = input().lower().split()
summ = s.count('a') + s.count('an') + s.count('the')
print('Общее количество артиклей:', summ)         
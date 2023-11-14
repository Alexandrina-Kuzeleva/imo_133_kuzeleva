'''2 5 10
1 2
1 2 3 4 5
1 A 3
1 A 4
1 A 5
1 A 6
1 A 7
-1 A 1
1 B 7
-1 A 6
-1 B 1
1 A 7'''

N = int(input())
M = int(input())
Q = int(input())
N_col = input().split()
M_col =  input().split()

G = [input().split() for i in range(1,int(Q)+1)]

for i in G:
    if i[1] == "A":
        if i[1]=='1':
            N_col.append(i[2])
        else:
            N_col.remove(i[2])
    else:
        if i[1]=='1':
            M_col.append(i[2])
        else:
            M_col.remove(i[2])
print(N_col, M_col)

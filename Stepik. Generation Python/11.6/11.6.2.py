s = [int(i) for i in input().split()]
index_mx = s.index(max(s))
index_mn = s.index(min(s))

s[index_mx], s[index_mn ] = min(s), max(s)
print(*s)
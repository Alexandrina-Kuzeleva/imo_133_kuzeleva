numbers = [int(i) for i in input().split()]
numbers.sort()
print(*numbers)
numbers.sort(reverse=True)
print(*numbers)
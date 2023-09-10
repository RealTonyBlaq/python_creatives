#!/usr/bin/python3

a = 0
while a < 6:
	print(a, end=' ')
	a += 1
print()
lists = [1, 2, 3, 4, 5]
copy = lists
lists.append(10)
lists[1] = 20
print(copy)
print(lists)
print(lists[0])
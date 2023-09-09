#!/usr/bin/python3

a = 0
while a < 6:
	print(a, end=' ')
	a = a + 1
print()
lists = [1, 2, 3, 4, 5]
for i in range(len(lists)):
	print(lists[i], end='\t  ')
	print(lists[i])
print(0, end=' ')
for i in range(len(lists)):
	print(lists[i], end=' ')
print()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("lenght of matrix is", len(matrix))
for i in range(0, 3):
	for j in matrix[i]:
		print("{:d}".format(j), end=" ")
	print()
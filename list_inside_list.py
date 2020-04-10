# List Inside List
matrix = [[1,2,3], [4,5,6,], [7,8,9]] # 2D List
# 3 Items
print(matrix[0]) # Output : [1, 2, 3]
print(matrix[1]) # Output : [4, 5, 6]
print(matrix[2]) # Output : [7, 8, 9]
# Start Loop
for i in matrix:
    print(i)
# For Loop Inside For Loop
for sublist in matrix:
    for i in sublist:
        print(i)
print(matrix[1][1]) # Output : 5
print(matrix[2][0]) # Output : 7
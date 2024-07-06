"""
for diginext 
example 1 
sajjad esmaili 
7/06/2024
"""

def searchMatrix(matrix, target):
    """
    
    """
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    row, col = 0, n - 1

    while row < m and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1

    return False

matrix = [[1, 3, 5], [7, 8, 10], [12, 15, 18]]
target = 8
print(searchMatrix(matrix, target)) 


%--2 
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    low, high = 0, m * n - 1

    while low <= high:
        mid = (low + high) // 2
        row, col = divmod(mid, n)
        mid_value = matrix[row][col]

        if mid_value == target:
            return True
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

matrix = [[1, 3, 5], [7, 8, 10], [12, 15, 18]]
target = 8
print(searchMatrix(matrix, target))  


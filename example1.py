"""
for diginext 
example 1 
sajjad esmaili 
7/06/2024
"""

"""
سوال: یک الگوریتم کارآمد بنویسید که یک مقدار هدف را در یک ماتریس m*n جستجو کند. این ماتریس دارای خصوصیات زیر است: اعداد در هر ردیف از چپ به راست مرتب شده‌اند و اولین عدد هر ردیف بزرگتر از آخرین عدد ردیف قبلی است.



مفهوم آزمون: ترکیب جستجوی دودویی با پیمایش ماتریس.



توضیحات:

در این ماتریس، با توجه به مرتب بودن اعداد در هر ردیف و ترتیب خاص بین ردیف‌ها، می‌توان از روش جستجوی دودویی برای پیدا کردن مقدار هدف استفاده کرد. ابتدا ماتریس به صورت یک بعدی در نظر گرفته می‌شود و سپس جستجوی دودویی روی آن انجام می‌گیرد.



مثال: 

- ورودی:[[1, 3, 5], [7, 8, 10], [12, 15, 18]], هدف: ۸

- خروجی: True

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


"""
for diginext 
example 1 
sajjad esmaili 
7/06/2024
"""

"""
توضیحات سوال
سوال: با توجه به یک آرایه نامرتب از اعداد صحیح، طولانی‌ترین دنباله عناصر متوالی را پیدا کنید.

مفهوم آزمون: استفاده از مجموعه درهم‌سازی برای پیگیری عناصر و بررسی دنباله‌های متوالی.

توضیحات:

برای یافتن طولانی‌ترین دنباله متوالی، ابتدا اعداد را در یک مجموعه ذخیره می‌کنیم و سپس برای هر عدد بررسی می‌کنیم که آیا آغازگر یک دنباله جدید است یا خیر. در صورتی که آغازگر باشد، طول دنباله را محاسبه کرده و بزرگترین طول را ذخیره می‌کنیم.

مثال:

- ورودی: [100, 4, 200, 1, 3, 2]

- خروجی: 4 (دنباله: [1, 2, 3, 4])
"""

def longestConsecutive(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in nums:
        if num - 1 not in num_set:
            current_streak = 1
            while num + current_streak in num_set:
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)

    return longest_streak

input_nums = [100, 4, 200, 1, 3, 2,5]
print(longestConsecutive(input_nums))  

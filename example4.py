"""
for diginext 
example 1 
sajjad esmaili 
7/06/2024
"""

"""
سوال: با توجه به یک مجموعه از بازه‌ها، همه بازه‌های هم‌پوشانی شده را ادغام کنید.

مفهوم آزمون: ادغام و مرتب‌سازی بازه‌ها.

توضیحات:

برای ادغام بازه‌ها، ابتدا بازه‌ها را بر اساس نقطه شروع آنها مرتب می‌کنیم. سپس، با پیمایش بازه‌های مرتب شده، بازه‌های هم‌پوشانی را با هم ادغام می‌کنیم و تنها بازه‌های غیر هم‌پوشانی را نگه می‌داریم.

مثال:

- ورودی:[(1, 3), (2, 6), (8, 10)]

- خروجی: [(1, 6), (8, 10)]
"""

def mergeIntervals(intervals):
 
    if not intervals:
        return []

 
    intervals.sort(key=lambda x: x[0])

 
    merged = []

 
    current_start, current_end = intervals[0]

    for interval in intervals[1:]:
        start, end = interval
        if start <= current_end:  # هم‌پوشانی بازه‌ها
            current_end = max(current_end, end)  # ادغام بازه‌ها
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end

 
    merged.append((current_start, current_end))

    return merged

 
input_intervals = [(1, 3), (2, 6), (8, 10)]
print(mergeIntervals(input_intervals))   

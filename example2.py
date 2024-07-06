"""
for diginext 
example 1 
sajjad esmaili 
7/06/2024
"""


"""
سوال: با توجه به یک آرایه از رشته‌ها، آنگرام‌ها را با هم گروه‌بندی کنید.

مفهوم آزمون: استفاده از جدول درهم‌سازی با رشته‌های مرتب شده به عنوان کلید.

توضیحات:

در این سوال، هدف این است که رشته‌هایی که ترکیب حروف یکسان دارند (آنگرام‌ها) را در یک گروه قرار دهیم. با مرتب کردن حروف هر رشته و استفاده از آن به عنوان کلید در جدول درهم‌سازی، می‌توان رشته‌ها را به سادگی گروه‌بندی کرد.

مثال:

- ورودی: ["eat", "tea", "tan", "ate", "nat", "bat"]

- خروجی: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""

from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)

    for s in strs:

        key = ''.join(sorted(s))
        anagrams[key].append(s)

        vls = list(anagrams.values())
    return vls 

input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(input_strs))

# count number of digits-
"""
n = int(input("Enter a number: "))
count = 0
while n > 0:
    count += 1
    n = n // 10
print("The number of digits are: ", count)
# T.C=O(log10(n))
"""

# check pallindrome-
num = int(input("Enter a number: "))
temp_num = num
new = 0
while temp_num > 0:
    new = new * 10 + temp_num % 10
    temp_num = temp_num // 10
if new == num:
    print("pallindrome")
else:
    print("Not pallindrome")
# T.C-O(log10(n));

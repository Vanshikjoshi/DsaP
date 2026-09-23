# count number of digits-

n = int(input("Enter a number: "))
count = 0
while n > 0:
    count += 1
    n = n // 10
print("The number of digits are: ", count)
# T.C=O(log10(n))


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


# armstrong number-
arm_num = int(input("Enter the number: "))
length = len(str(arm_num))
new_arm_num = arm_num
print(length)
num_new = 0
while new_arm_num > 0:
    num_new = (new_arm_num % 10) ** length + num_new
    new_arm_num = new_arm_num // 10
if arm_num == num_new:
    print("Armstrong!")
else:
    print("Not armstrong")
# T.C - O(log10(n));

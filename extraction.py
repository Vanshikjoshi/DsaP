# count number of digits-
n = int(input("Enter a number: "))
count = 0
while n > 0:
    count += 1
    n = n // 10
print("The number of digits are: ", count)
# T.C=O(log10(n))

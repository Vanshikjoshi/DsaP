"""
Expected output-
*****
*****
*****
*****
*****

"""


def squarestar(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()


squarestar(5)

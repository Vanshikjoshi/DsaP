"""
Expected output-
*
**
***
****
*****

"""


def rightangledstar(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end="")
        print()


rightangledstar(5)


"""
invertd right-angled star triangle
Expected output-
*****
****
***
**
*
"""


def invertedrightangledstar(n):
    for i in range(n):
        for j in range(n - i):
            print("*", end="")
        print()


invertedrightangledstar(5)
